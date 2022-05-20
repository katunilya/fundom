from typing import Callable, TypeVar

from pymon.core import hof_2

TKey = TypeVar("TKey")
TValue = TypeVar("TValue")


@hof_2
def maybe_get(key: TKey, dct: dict[TKey, TValue]) -> TValue | None:
    """Maybe get some value from dictionary.

    Args:
        key (TKey): of dict.
        dct (dict[TKey, TValue]): dictionary.

    Returns:
        TValue | None: value of key if one is present.
    """
    return dct.get(key, None)


T = TypeVar("T")


@hof_2
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
