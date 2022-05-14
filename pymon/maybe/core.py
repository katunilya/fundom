from __future__ import annotations

from dataclasses import dataclass
from functools import wraps
from typing import Any, Awaitable, Callable, TypeVar

from pymon.core import Future, MonadContainer, V, this_async

# containers


T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class Some(MonadContainer[T]):
    ...


@dataclass(frozen=True, slots=True)
class Nothing:
    __instance: Nothing | None

    def __new__(cls, *args, **kwargs) -> Nothing:  # noqa
        match cls.__instance:
            case None:
                cls.__instance = object.__new__(cls)
                return cls.__instance
            case _:
                return cls.__instance

    def __init__(self) -> None:  # noqa
        ...


Maybe = Some[T] | Nothing


def maybe_unit(value: T | None) -> Maybe[T]:
    match value:
        case None:
            return Nothing()
        case _:
            return Some(value)


# bindings


def if_some(func: Callable[[T], Maybe[V]]):
    @wraps(func)
    def _wrapper(arg: Maybe[T]) -> Maybe[V]:
        match arg:
            case Some(value):
                return func(value)
            case Nothing():
                return Nothing()

    return _wrapper


def if_nothing(func: Callable[[Any], Maybe[V]]):
    @wraps(func)
    def _wrapper(arg: Maybe[T]) -> Maybe[V] | Maybe[T]:
        match arg:
            case Nothing() as nothing:
                return func(nothing)
            case Some() as some:
                return some

    return _wrapper


def if_some_async(func: Callable[[T], Awaitable[Maybe[V]]]):
    @wraps(func)
    def _wrapper(arg: Maybe[T]) -> Awaitable[Maybe[V]]:
        match arg:
            case Some(value):
                return Future(func(value))
            case Nothing():
                return Future(this_async(Nothing()))

    return _wrapper


def if_nothing_async(func: Callable[[Any], Awaitable[Maybe[V]]]):
    @wraps(func)
    def _wrapper(arg: Maybe[T]) -> Future[Maybe[V] | Maybe[T]]:
        match arg:
            case Nothing() as nothing:
                return Future(func(nothing))
            case Some() as some:
                return Future(this_async(some))

    return _wrapper


# utils
