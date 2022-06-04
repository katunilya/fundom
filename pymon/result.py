from dataclasses import dataclass
from functools import wraps
from typing import Awaitable, Callable, ParamSpec, TypeVar

from pymon.core import Future, hof1, hof2, returns_future, this, this_async

V = TypeVar("V")
T = TypeVar("T")
TError = TypeVar("TError", bound=Exception)


def if_ok(func: Callable[[T], V]):
    """Decorateor that protects function from being executed on `Exception` value."""

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


def safe_future(func: Callable[P, Awaitable[V]]) -> Callable[P, Future[V | TError]]:
    """Decorator for async function that might raise an exception.

    Excepts exception and returns that instead.
    """

    @wraps(func)
    @returns_future
    async def _wrapper(*args: P.args, **kwargs: P.kwargs) -> V | TError:
        try:
            return await func(*args, **kwargs)
        except Exception() as err:
            return err

    return _wrapper


async def _async_ternary(
    condition: Future[bool], error: TError, value: T
) -> Future[T] | Future[TError]:
    return value if await condition else error


@hof2
def ok_when(predicate: Callable[[T], bool], error: TError, value: T) -> T | TError:
    """Pass value only if predicate is True, otherwise return error.

    Args:
        predicate (Callable[[T], bool]): to fulfill.
        error (TError): to replace with.
        value (T): to process.

    Returns:
        T | TError: result.
    """
    match predicate(value):
        case True:
            return value
        case False:
            return error


@hof2
def ok_when_future(
    predicate: Callable[[T], bool], error: TError, value: T
) -> Future[T] | Future[TError]:
    """Pass value only if async predicate is True, otherwise return error.

    Args:
        predicate (Callable[[T], bool]): to fulfill.
        error (TError): to replace with.
        value (T): to process.

    Returns:
        Future[T] | Future[TError]: result.
    """
    return Future(_async_ternary(predicate, error, value))


@dataclass(slots=True, frozen=True)
class PolicyViolationError(Exception):
    """Exception that marks that policy is violated."""

    message: str


def check(predicate: Callable[P, bool]) -> T | PolicyViolationError:
    """Pass value next only if predicate is True, otherwise policy is violated.

    Args:
        predicate (Predicate[T]): to check.

    Returns:
        T | PolicyViolationError: result
    """
    return ok_when(predicate, PolicyViolationError(message=str(predicate)))


def check_future(
    predicate: Callable[P, Future[bool]]
) -> Future[T] | Future[PolicyViolationError]:
    """Pass value next only if predicate is True, otherwise policy is violated.

    Args:
        predicate (Callable[P, Future[bool]]): to check.

    Returns:
        Future[T] | Future[PolicyViolationError]: result.
    """
    return ok_when_future(predicate, PolicyViolationError(message=str(predicate)))


def choose_ok(*funcs: Callable[[T], V | TError]) -> Callable[[T], V | TError]:
    """Combines multiple functions that might return error into one.

    Result of the first function to return non-Exception result is returned.
    """
    match funcs:
        case []:
            return this
        case _:

            def _choose(value: T) -> V | TError:
                for func in funcs:
                    match func(value):
                        case Exception():
                            continue
                        case success:
                            return success

            return _choose


def choose_ok_future(
    *funcs: Callable[[T], Future[V] | Future[TError]]
) -> Callable[[T], Future[V] | Future[TError]]:
    """Combines multiple functions that might return error into one.

    Result of the first function to return non-Exception result is returned.
    """
    match funcs:
        case []:
            return returns_future(this_async)
        case _:

            @returns_future
            async def _choose(value: T) -> V | TError:
                for func in funcs:
                    match func(value):
                        case Future() as f:
                            match await f:
                                case Exception():
                                    continue
                                case success:
                                    return success
                        case Exception():
                            continue
                        case success:
                            return success

            return _choose
