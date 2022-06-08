from typing import TypeVar

from pymon.core import hof1
from pymon.result import safe

TKey = TypeVar("TKey")
TValue = TypeVar("TValue")


@hof1
@safe
def try_get(key: TKey, arg: dict[TKey, TValue]) -> TValue:
    """Point-free version of `dict[key]`.

    Error-safe, returns `KeyError` in case key is not present and  `__missing__()` is
    not provided.

    Args:
        key (TKey): to get.
        arg (dict[TKey, TValue]): to get from.

    Returns:
        TValue: value.
    """
    return arg[key]


@hof1
def maybe_get(key: TKey, arg: dict[TKey, TValue]) -> TValue | None:
    """Point-free version if `dict.get` with default `None`.

    Args:
        key (TKey): to get.
        arg (dict[TKey,TValue]): to get from.

    Returns:
        TValue | None: value.
    """
    return arg.get(key, None)
