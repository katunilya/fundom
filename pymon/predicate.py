from __future__ import annotations

from dataclasses import dataclass
from typing import Awaitable, Callable, Iterable, ParamSpec, Sized, TypeVar

from pymon.core import _compose_future, compose

P = ParamSpec("P")


class FuturePredicate(_compose_future[P, bool]):
    """Abstraction over async predicates."""

    func: Callable[P, Awaitable[bool]]

    def __mul__(self, other: Callable[P, bool]) -> FuturePredicate[P]:
        def _mul(other: Callable[P, Awaitable[bool]]):
            async def __mul(*args: P.args, **kwargs: P.kwargs) -> bool:
                return await self.func(*args, **kwargs) and other(*args, **kwargs)

            return __mul

        return FuturePredicate(_mul(other))

    def __add__(self, other: Callable[P, bool]) -> FuturePredicate[P]:
        def _add(other: Callable[P, Awaitable[bool]]):
            async def __add(*args: P.args, **kwargs: P.kwargs) -> bool:
                return await self.func(*args, **kwargs) or other(*args, **kwargs)

            return __add

        return FuturePredicate(_add(other))

    def __and__(self, other: Callable[P, Awaitable[bool]]) -> FuturePredicate[P]:
        def _and(other: Callable[P, Awaitable[bool]]):
            async def __and(*args: P.args, **kwargs: P.kwargs) -> bool:
                return await self.func(*args, **kwargs) and await other(*args, **kwargs)

            return __and

        return FuturePredicate(_and(other))

    def __or__(self, other: Callable[P, Awaitable[bool]]) -> Predicate[P]:
        def _or(other: Callable[P, Awaitable[bool]]):
            async def __or(*args: P.args, **kwargs: P.kwargs) -> bool:
                return await self.func(*args, **kwargs) or await other(*args, **kwargs)

            return __or

        return FuturePredicate(_or(other))

    def __invert__(self) -> FuturePredicate[P]:
        async def _invert(*args, **kwargs) -> bool:
            return not await self.func(*args, **kwargs)

        return FuturePredicate(_invert)


@dataclass(slots=True, frozen=True)
class Predicate(compose[P, bool]):
    """Abstraction over predicates."""

    func: Callable[P, bool]

    def __mul__(self, other: Callable[P, bool]) -> Predicate[P]:
        def _mul(*args: P.args, **kwargs: P.kwargs) -> bool:
            return self.func(*args, **kwargs) and other(*args, **kwargs)

        return Predicate(_mul)

    def __add__(self, other: Callable[P, bool]) -> Predicate[P]:
        def _add(*args: P.args, **kwargs: P.kwargs) -> bool:
            return self.func(*args, **kwargs) or other(*args, **kwargs)

        return Predicate(_add)

    def __and__(self, other: Callable[P, Awaitable[bool]]) -> FuturePredicate[P]:
        def _and(other: Callable[P, Awaitable[bool]]):
            async def __and(*args: P.args, **kwargs: P.kwargs) -> bool:
                return self.func(*args, **kwargs) and await other(*args, **kwargs)

            return __and

        return FuturePredicate(_and(other))

    def __or__(self, other: Callable[P, Awaitable[bool]]) -> FuturePredicate[P]:
        def _or(other: Callable[P, Awaitable[bool]]):
            async def __or(*args: P.args, **kwargs: P.kwargs) -> bool:
                return self.func(*args, **kwargs) or await other(*args, **kwargs)

            return __or

        return FuturePredicate(_or(other))

    def __invert__(self) -> Predicate[P]:
        def _invert(*args: P.args, **kwargs: P.kwargs):
            return not self.func(*args, **kwargs)

        return Predicate(_invert)


def predicate(p: Callable[P, bool]):
    """Makes function composable `Predicate` instance."""
    return Predicate(p)


def future_predicate(p: Callable[P, Awaitable[bool]]):
    """Makes function composable `FuturePredicate` instance."""
    return FuturePredicate(p)


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
