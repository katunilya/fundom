from typing import Callable, TypeVar

from pymon.core import hof_2
from pymon.maybe.core import Maybe, Nothing, Some, maybe_unit

TKey = TypeVar("TKey")
TValue = TypeVar("TValue")


@hof_2
def maybe_get(key: TKey, data: dict[TKey, TValue]) -> Maybe[TValue]:
    return maybe_unit(data.get(key, None))


T = TypeVar("T")


@hof_2
def maybe_when(predicate: Callable[[T], bool], data: T) -> Maybe[T]:
    match predicate(data):
        case True:
            return Some(data)
        case False:
            return Nothing()
