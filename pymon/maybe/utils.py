from typing import Callable, TypeVar

from pymon.core import hof1

T = TypeVar("T")


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
