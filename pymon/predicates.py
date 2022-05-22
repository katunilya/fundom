from typing import Iterable

from pymon.core import hof1


@hof1
def len_more_then(length: int, iterable: Iterable) -> bool:
    """If `iterable` length is strictly more than `length`."""
    return length < len(iterable)
