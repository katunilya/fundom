from functools import wraps
from typing import Callable, TypeVar

from pymon.core import hof_2

T = TypeVar("T")
V = TypeVar("V")


def if_some(func: Callable[[T], V | None]) -> Callable[[T | None], V | None]:
    """Decorator that protects function from being executed on `None` value."""

    @wraps(func)
    def _wrapper(t: T | None) -> V | None:
        match t:
            case None:
                return None
            case some:
                return func(some)

    return _wrapper


def if_none(func: Callable[[None], V]) -> Callable[[T | None], V | None]:
    """Decorator that executes some function only on `None` input."""

    @wraps(func)
    def _wrapper(t: T | None) -> V | None:
        match t:
            case None:
                return func(None)
            case some:
                return some

    return _wrapper


@hof_2
def if_none_returns(replacement: V, value: T | None) -> V | T:
    """Replace `value` with `replacement` if one is `None`.

    Args:
        replacement (V): to replace with.
        value (T | None): to replace.

    Returns:
        V | T: some result.
    """
    match value:
        case None:
            return replacement
        case some:
            return some
