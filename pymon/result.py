from functools import wraps
from typing import Awaitable, Callable, ParamSpec, TypeVar

from pymon.core import future, hof1, hof2, this, this_future

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

    Args:
        predicate (Callable[[T], bool]): to fulfill.
        create_error (Callable[[T], TError]): factory function for error.
        value (T): to process.

    Returns:
        Future[T] | Future[TError]: result.
    """
    return future(__check_future(predicate, create_error, value))


def choose_ok(*funcs: Callable[[T], V | TError]) -> Callable[[T], V | TError]:
    """Combines multiple sync functions that might return error into one.

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
    *funcs: Callable[[T], future[V | TError]]
) -> Callable[[T], future[V | TError]]:
    """Combines multiple async functions that might return error into one.

    Result of the first function to return non-Exception result is returned.
    """
    match funcs:
        case []:
            return this_future
        case _:

            @future.returns
            async def _choose(value: T) -> V | TError:
                for func in funcs:
                    match await func(value):
                        case Exception():
                            continue
                        case success:
                            return success

            return _choose
