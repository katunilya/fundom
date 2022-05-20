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
