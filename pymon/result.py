from __future__ import annotations

import copy
from dataclasses import dataclass
from functools import wraps
from typing import Awaitable, Callable, Generic, ParamSpec, TypeVar

from pymon.core import future, hof1, hof2

V = TypeVar("V")
T = TypeVar("T")
TError = TypeVar("TError", bound=Exception)


def if_ok(func: Callable[[T], V]):
    """Decorator that protects function from being executed on `Exception` value."""

    @wraps(func)
    def _wrapper(t: T) -> V:
        match t:
            case Exception():
                return t
            case ok:
                return func(ok)

    return _wrapper


def if_error(func: Callable[[T], V]):
    """Decorator that executes some function only on `Exception` input."""

    @wraps(func)
    def _wrapper(t: T) -> V | Exception:
        match t:
            case Exception():
                return func(t)
            case _:
                return t

    return _wrapper


@hof1
def if_error_returns(replacement: V, value: T) -> V | T:
    """Replace `value` with `replacement` if one is `Exception`.

    Args:
        replacement (V): to replace with.
        value (T | TError): to replace.

    Returns:
        V | T: error-safe result.
    """
    match value:
        case Exception():
            return replacement
        case _:
            return value


P = ParamSpec("P")


def safe(func: Callable[P, V]) -> Callable[P, V | Exception]:
    """Decorator for sync function that might raise an exception.

    Excepts exception and returns that instead.
    """

    @wraps(func)
    def _wrapper(*args: P.args, **kwargs: P.kwargs) -> V | Exception:
        try:
            return func(*args, **kwargs)
        except Exception() as err:
            return err

    return _wrapper


def safe_future(func: Callable[P, Awaitable[V]]) -> Callable[P, future[V | TError]]:
    """Decorator for async function that might raise an exception.

    Excepts exception and returns that instead.
    """

    @wraps(func)
    @future.returns
    async def _wrapper(*args: P.args, **kwargs: P.kwargs) -> V | TError:
        try:
            return await func(*args, **kwargs)
        except Exception() as err:
            return err

    return _wrapper


@hof2
def check(
    predicate: Callable[[T], bool], create_error: Callable[[T], TError], value: T
) -> T | TError:
    """Pass value only if predicate is True, otherwise return error.

    Examples::

            policy = check(lambda x: x > 10, lambda _: Exception("More than 10"))

    Args:
        predicate (Callable[[T], bool]): to fulfill.
        create_error (Callable[[T], TError]): factory function for error.
        value (T): to process.

    Returns:
        T | TError: result.
    """
    return value if predicate(value) else create_error(value)


async def __check_future(
    predicate: Callable[[T], Awaitable[bool]],
    create_error: Callable[[T], TError],
    value: T,
) -> future[T] | future[TError]:
    return value if await predicate(value) else create_error(value)


@hof2
def check_future(
    predicate: Callable[[T], Awaitable[bool]],
    create_error: Callable[[T], TError],
    value: T,
) -> future[T] | future[TError]:
    """Pass value only if async predicate is True, otherwise return error.

    Examples::

            policy = check_future(more_than_10, lambda _: Exception("More than 10"))

    Args:
        predicate (Callable[[T], bool]): to fulfill.
        create_error (Callable[[T], TError]): factory function for error.
        value (T): to process.

    Returns:
        future[T] | future[TError]: result.
    """
    return future(__check_future(predicate, create_error, value))


class EmptyChooseOkError(Exception):
    """Returned when `choose_ok` or `choose_ok_future` has no options."""


class FailedChooseOkError(Exception, Generic[P]):
    """Returned when no function in `choose_ok` or `choose_ok_future` succeeded."""

    def __init__(self, *args: P.args, **_: P.kwargs) -> None:
        self.args = args


@dataclass(slots=True, init=False)
class choose_ok(Generic[P, T]):  # noqa
    """Combines multiple sync functions into switch-case like statement.

    The first function to return non-`Exception` result is used. If no function passed
    than `EmptyChooseOkError` is raised. Uses deepcopy to keep arguments immutable
    during attempts.

    Examples::

            f = (
                choose_ok()
                | create_linked_node
                | create_isolated_node
            )
    """

    funcs: list[Callable[P, T | TError]]

    def __init__(self) -> None:
        self.funcs = []

    def __call__(self, *args: P.args, **_: P.kwargs) -> T | TError:  # noqa
        if len(self.funcs) == 0:
            return EmptyChooseOkError()

        for func in self.funcs:
            copy_args = copy.deepcopy(args)
            match func(*copy_args):
                case Exception():
                    continue
                case ok:
                    return ok

        return FailedChooseOkError(*args)

    def __or__(self, option: Callable[P, T]) -> choose_ok[P, T]:
        self.funcs.append(option)
        return self


@dataclass(slots=True, init=False)
class choose_ok_future(Generic[P, T]):  # noqa
    """Combines multiple async functions into switch-case like statement.

    The first function to return non-`Exception` result is used. If no function passed
    than `EmptyChooseOkError` is raised. Uses deepcopy to keep arguments immutable
    during attempts.

    Examples::

            f = (
                choose_ok_future()
                | create_linked_node
                | create_isolated_node
            )
    """

    funcs: list[Callable[P, T | TError]]

    def __init__(self) -> None:
        self.funcs = []

    @future.returns
    async def __call__(self, *args: P.args, **_: P.kwargs) -> T | TError:  # noqa
        if len(self.funcs) == 0:
            return EmptyChooseOkError()

        for func in self.funcs:
            copy_args = copy.deepcopy(args)
            match await func(*copy_args):
                case Exception():
                    continue
                case ok:
                    return ok

        return FailedChooseOkError(*args)

    def __or__(self, option: Callable[P, T]) -> choose_ok[P, T]:
        self.funcs.append(option)
        return self
