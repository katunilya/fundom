from dataclasses import dataclass
from typing import Callable, Iterable, ParamSpec, Sized, TypeVar

from pymon.core import Func, Future

P = ParamSpec("P")
TBool = TypeVar("TBool", bool, Future[bool])


@dataclass(slots=True, frozen=True)
class Predicate(Func[P, TBool]):
    """Abstraction over predicates for seamless composition of predicate functions."""

    func: Callable[P, TBool]

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> TBool:  # noqa
        return self._predicate(*args, **kwargs)

    def __and__(self, other: "Predicate[P, TBool]") -> "Predicate[P, TBool]":
        return Predicate(lambda v: self._predicate(v) and other._predicate(v))

    def __or__(self, other: "Predicate[P, TBool]") -> "Predicate[P, TBool]":
        return Predicate(lambda v: self._predicate(v) or other._predicate(v))

    def __invert__(self) -> "Predicate[P, TBool]":
        return Predicate(lambda v: not self._predicate(v))


def predicate(func: Callable[P, TBool]):
    """Makes function composable `Predicate` instance."""
    return Predicate(func)


def len_more_then(length: int):
    """If `iterable` length is strictly more than `length`."""

    @predicate
    def _predicate(iterable: Iterable) -> bool:
        return length < len(iterable)

    return _predicate


def len_less_then(length: int):
    """If `iterable` length is strictly less than `length`."""

    @predicate
    def _predicate(iterable: Iterable) -> bool:
        return length > len(iterable)

    return _predicate


def len_less_or_equals(length: int):
    """If `iterable` length is less or equals `length`."""

    @predicate
    def _predicate(iterable: Iterable) -> bool:
        return len(iterable) <= length

    return _predicate


def len_more_or_equals(length: int):
    """If `iterable` length is more or equals `length`."""

    @predicate
    def _predicate(iterable: Iterable) -> bool:
        return len(iterable) >= length

    return _predicate


TSized = TypeVar("TSized", bound=Sized)


@predicate
def is_empty(obj: TSized) -> bool:
    """If `obj` is empty."""
    return len(obj) == 0


@predicate
def is_not_empty(obj: TSized) -> bool:
    """If `obj` is not empty."""
    return len(obj) != 0
