from __future__ import annotations

from typing import Iterable, Sized, TypeVar


def len_more_then(length: int):
    """If `iterable` length is strictly more than `length`."""

    def _predicate(iterable: Iterable) -> bool:
        return length < len(iterable)

    return _predicate


def len_less_then(length: int):
    """If `iterable` length is strictly less than `length`."""

    def _predicate(iterable: Iterable) -> bool:
        return length > len(iterable)

    return _predicate


def len_less_or_equals(length: int):
    """If `iterable` length is less or equals `length`."""

    def _predicate(iterable: Iterable) -> bool:
        return len(iterable) <= length

    return _predicate


def len_more_or_equals(length: int):
    """If `iterable` length is more or equals `length`."""

    def _predicate(iterable: Iterable) -> bool:
        return len(iterable) >= length

    return _predicate


TSized = TypeVar("TSized", bound=Sized)


def is_empty(obj: TSized) -> bool:
    """If `obj` is empty."""
    return len(obj) == 0


def is_not_empty(obj: TSized) -> bool:
    """If `obj` is not empty."""
    return len(obj) != 0
