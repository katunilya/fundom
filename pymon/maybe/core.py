from functools import wraps
from typing import Callable, TypeVar

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
