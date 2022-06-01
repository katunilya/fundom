from typing import Iterable, Sized, TypeVar

from pymon.core import hof1


@hof1
def len_more_then(length: int, iterable: Iterable) -> bool:
    """If `iterable` length is strictly more than `length`."""
    return length < len(iterable)


@hof1
def len_less_then(length: int, iterable: Iterable) -> bool:
    """If `iterable` length is strictly less than `length`."""
    return length > len(iterable)


@hof1
def len_less_or_equals(length: int, iterable: Iterable) -> bool:
    """If `iterable` length is less or equals `length`."""
    return len(iterable) <= length


@hof1
def len_more_or_equals(length: int, iterable: Iterable) -> bool:
    """If `iterable` length is more or equals `length`."""
    return len(iterable) >= length


TSized = TypeVar("TSized", bound=Sized)


def is_empty(obj: TSized) -> bool:
    """If `obj` is empty."""
    return len(obj) == 0


def is_not_empty(obj: TSized) -> bool:
    """If `obj` is not empty."""
    return len(obj) != 0
