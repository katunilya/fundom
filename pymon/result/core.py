from functools import wraps
from typing import Callable, ParamSpec, TypeVar

from pymon.core import hof1

V = TypeVar("V")
T = TypeVar("T")
TError = TypeVar("TError", bound=Exception)


def if_ok(func: Callable[[T], V]) -> Callable[[T | TError], V]:
    """Decorateor that protects function from being executed on `Exception` value."""

    @wraps(func)
    def _wrapper(t: T | TError) -> V:
        match t:
            case Exception():
                return t
            case ok:
                return func(ok)

    return _wrapper


def if_error(func: Callable[[TError], V]) -> Callable[[T | TError], T | V]:
    """Decorator that executes some function only on `Exception` input."""

    @wraps(func)
    def _wrapper(t: T | TError) -> T | V:
        match t:
            case Exception():
                return func(t)
            case _:
                return t

    return _wrapper


@hof1
def if_error_returns(replacement: V, value: T | TError) -> V | T:
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


def safe(func: Callable[P, V]) -> Callable[P, V | TError]:
    """Decorator for sync function that might raise an exception.

    Excepts exception and returns that instead.
    """

    @wraps(func)
    def _wrapper(*args: P.args, **kwargs: P.kwargs) -> V | TError:
        try:
            return func(*args, **kwargs)
        except Exception() as err:
            return err

    return _wrapper
