from functools import wraps
from typing import Callable, TypeVar

from pymon.core import hof1

T = TypeVar("T")
V = TypeVar("V")


def if_some(func: Callable[[T], V]):
    """Decorator that protects function from being executed on `None` value."""

    @wraps(func)
    def _wrapper(t: T):
        match t:
            case None:
                return None
            case some:
                return func(some)

    return _wrapper


def if_none(func: Callable[[T], V]):
    """Decorator that executes some function only on `None` input."""

    @wraps(func)
    def _wrapper(t: T) -> V | None:
        match t:
            case None:
                return func(None)
            case some:
                return some

    return _wrapper


@hof1
def if_none_returns(replacement: V, value: T) -> V | T:
    """Replace `value` with `replacement` if one is `None`.

    Args:
        replacement (V): to replace with.
        value (T): to replace.

    Returns:
        V | T: some result.
    """
    match value:
        case None:
            return replacement
        case some:
            return some


@hof1
def some_when(predicate: Callable[[T], bool], data: T) -> T | None:
    """Passes value next only when predicate is True, otherwise returns `None`.

    Args:
        predicate (Callable[[T], bool]): to fulfill.
        data (T): to process.

    Returns:
        T | None: retult.
    """
    match predicate(data):
        case True:
            return data
        case False:
            return None
