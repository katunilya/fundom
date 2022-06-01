from functools import wraps
from typing import Awaitable, Callable, ParamSpec, TypeVar

from pymon.core import hof1

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


def safe_async(
    func: Callable[P, Awaitable[V]]
) -> Callable[P, Awaitable[V | Exception]]:
    """Decorator for async function that might raise an exception.

    Excepts exception and returns that instead.
    """

    @wraps(func)
    async def _wrapper(*args: P.args, **kwargs: P.kwargs) -> V | Exception:
        try:
            return await func(*args, **kwargs)
        except Exception() as err:
            return err

    return _wrapper
