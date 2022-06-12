from __future__ import annotations

from dataclasses import dataclass
from typing import Awaitable, Callable, Generic, Iterable, ParamSpec, Sized, TypeVar

from pymon.core import future

P = ParamSpec("P")


@dataclass(slots=True, init=False)
class _each_future(Generic[P]):  # noqa
    sync_predicates: list[Callable[P, bool]]
    async_predicates: list[Callable[P, Awaitable[bool]]]

    def __init__(self) -> None:
        self.sync_predicates = []
        self.async_predicates = []

    @future.returns
    async def __call__(self, *args: P.args, **_: P.kwargs) -> bool:
        if (
            all(sync_predicate(*args) for sync_predicate in self.sync_predicates)
            is False
        ):
            return False

        for async_predicate in self.async_predicates:
            if await async_predicate(*args) is False:
                return False

        return True

    def __lshift__(self, nxt: Callable[P, bool]) -> _each_future[P]:
        self.sync_predicates.append(nxt)
        return self

    def __rshift__(self, nxt: Callable[P, Awaitable[bool]]) -> _each_future[P]:
        self.async_predicates.append(nxt)
        return self


@dataclass(slots=True, init=False)
class each(Generic[P]):  # noqa
    """Mathematical conjunction of predicates."""

    predicates: list[Callable[P, bool]]

    def __init__(self) -> None:
        self.predicates = []

    def __call__(self, *args: P.args, **_: P.kwargs) -> bool:  # noqa
        return all(predicate(*args) for predicate in self.predicates)

    def __lshift__(self, nxt: Callable[P, bool]) -> each[P]:
        self.predicates.append(nxt)
        return self

    def __rshift__(self, nxt: Callable[P, Awaitable[bool]]) -> _each_future[P]:
        ef = _each_future()

        for predicate in self.predicates:
            ef = ef << predicate

        return ef >> nxt


@dataclass(slots=True, init=False)
class _one_future(Generic[P]):  # noqa

    sync_predicates: list[Callable[P, bool]]
    async_predicates: list[Callable[P, Awaitable[bool]]]

    def __init__(self) -> None:
        self.sync_predicates = []
        self.async_predicates = []

    @future.returns
    async def __call__(self, *args: P.args, **_: P.kwargs) -> bool:
        if (
            any(sync_predicate(*args) for sync_predicate in self.sync_predicates)
            is True
        ):
            return True

        for async_predicate in self.async_predicates:
            if await async_predicate(*args) is True:
                return True

        return False

    def __lshift__(self, nxt: Callable[P, bool]) -> _each_future[P]:
        self.sync_predicates.append(nxt)
        return self

    def __rshift__(self, nxt: Callable[P, Awaitable[bool]]) -> _each_future[P]:
        self.async_predicates.append(nxt)
        return self


@dataclass(slots=True, init=False)
class one(Generic[P]):  # noqa
    """Mathematical disjunction of predicates."""

    predicates: list[Callable[P, bool]]

    def __init__(self) -> None:
        self.predicates = []

    def __call__(self, *args: P.args, **_: P.kwargs) -> bool:  # noqa
        return any(predicate(*args) for predicate in self.predicates)

    def __lshift__(self, nxt: Callable[P, bool]) -> one[P]:
        self.predicates.append(nxt)
        return self

    def __rshift__(self, nxt: Callable[P, Awaitable[bool]]) -> _one_future[P]:
        ef = _one_future()

        for predicate in self.predicates:
            ef = ef << predicate

        return ef >> nxt


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
