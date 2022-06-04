from dataclasses import dataclass
from typing import Callable, Iterable, Sized, TypeVar

from pymon.core import hof1

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class Predicate(Callable[[T], bool]):
    """Abstraction over predicates for seamless composition of predicate functions."""

    _predicate: Callable[[T], bool]

    def __call__(self, value: T) -> bool:  # noqa
        return self._predicate(value)

    def _and(self, other: "Predicate[T]") -> "Predicate[T]":
        return Predicate(lambda v: self._predicate(v) and other._predicate(v))

    def __and__(self, other: "Predicate[T]") -> "Predicate[T]":
        return self._and(other)

    def _or(self, other: "Predicate[T]") -> "Predicate[T]":
        return Predicate(lambda v: self._predicate(v) or other._predicate(v))

    def __or__(self, other: "Predicate[T]") -> "Predicate[T]":
        return self._or(other)

    def _invert(self) -> "Predicate[T]":
        return Predicate(lambda v: not self._predicate(v))

    def __invert__(self) -> "Predicate[T]":
        return self._invert()


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
