from dataclasses import dataclass

from typing import Callable, Generic, Iterable, Sized, TypeVar


T = TypeVar("T")


@dataclass(slots=True)
class Predicate(Generic[T]):
    """Abstraction over predicates for seamless composition of predicate functions."""

    _predicate: Callable[[T], bool]

    def __init__(self, predicate: Callable[[T], bool]) -> None:
        self._predicate = predicate

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


def predicate(func: Callable[[T], bool]) -> Predicate[T]:
    """Makes function composable `Predicate` instance."""
    return Predicate(func)


def len_more_then(length: int) -> Predicate[Iterable]:
    """If `iterable` length is strictly more than `length`."""
    return Predicate(lambda iterable: length < len(iterable))


def len_less_then(length: int) -> Predicate[Iterable]:
    """If `iterable` length is strictly less than `length`."""
    return Predicate(lambda iterable: length > len(iterable))


def len_less_or_equals(length: int) -> Predicate[Iterable]:
    """If `iterable` length is less or equals `length`."""
    return Predicate(lambda iterable: len(iterable) <= length)


def len_more_or_equals(length: int) -> Predicate[Iterable]:
    """If `iterable` length is more or equals `length`."""
    return Predicate(lambda iterable: len(iterable) >= length)


TSized = TypeVar("TSized", bound=Sized)


@predicate
def is_empty(obj: TSized) -> bool:
    """If `obj` is empty."""
    return len(obj) == 0


@predicate
def is_not_empty(obj: TSized) -> bool:
    """If `obj` is not empty."""
    return len(obj) != 0
