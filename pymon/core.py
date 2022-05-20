from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from functools import reduce, wraps
from typing import (
    Any,
    Awaitable,
    Callable,
    Concatenate,
    Generator,
    Generic,
    Iterable,
    ParamSpec,
    TypeVar,
)

T = TypeVar("T")
V = TypeVar("V")
U = TypeVar("U")
P = ParamSpec("P")


@dataclass(frozen=True, slots=True)
class MonadContainer(Generic[T], ABC):
    value: T


@dataclass(slots=True, frozen=True)
class Future(MonadContainer[Awaitable[T]]):
    def __await__(self) -> Generator[None, None, T]:
        return self.value.__await__()

    async def __then(self, func: Callable[[T], V]) -> V:
        return func(await self.value)

    def then(self, func: Callable[[T], V]) -> Future[V]:
        return Future(self.__then(func))

    async def __then_async(self, func: Callable[[T], Awaitable[V]]) -> V:
        return await func(await self.value)

    def then_async(self, func: Callable[[T], Awaitable[V]]) -> Future[V]:
        return Future(self.__then_async(func))

    def finish(self) -> Awaitable[T]:
        return self.value

    def __rshift__(self, func: Callable[[T], Awaitable[V]]) -> Future[V]:
        return self.then_async(func)

    def __lshift__(self, func: Callable[[T], V]) -> Future[V]:
        return self.then(func)


def returns_future(func: Callable[P, T]):
    """Wraps  returned value of async function to `Future`."""

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> Future[T]:
        match func(*args, **kwargs):
            case Future() as future:
                return future
            case awaitable:
                return Future(awaitable)

    return wrapper


@dataclass(slots=True, frozen=True)
class Pipe(MonadContainer[T]):
    def then(self, func: Callable[[T], V]) -> Pipe[V]:
        return Pipe(func(self.value))

    def then_async(self, func: Callable[[T], Awaitable[V]]) -> Future[V]:
        return Future(func(self.value))

    def __lshift__(self, func: Callable[[T], V]) -> Pipe[V]:
        return self.then(func)

    def __rshift__(self, func: Callable[[T], Awaitable[V]]) -> Future[V]:
        return self.then_async(func)

    def finish(self) -> T:
        return self.value


def pipeline(func: Callable[P, Pipe[T]]) -> Callable[P, T]:
    """Decorator for functions that return `Pipe` object for seamless unwrapping."""

    @wraps(func)
    def _wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        return func(*args, **kwargs).value

    return _wrapper


# identity utils


def this(x: T) -> T:
    return x


async def this_async(x: T) -> T:
    return x


def returns(x: T) -> Callable[[Any], T]:
    return lambda _: x


def returns_async(x: T) -> Callable[[Any], Future[T]]:
    async def _returns_async(_) -> T:
        return x

    return _returns_async


# curring utils
# TODO improve annotations for HOFs

A1 = TypeVar("A1")
A2 = TypeVar("A2")
A3 = TypeVar("A3")
A4 = TypeVar("A4")
A5 = TypeVar("A5")
A6 = TypeVar("A6")
AResult = TypeVar("AResult")


def hof1(func: Callable[Concatenate[A1, P], AResult]):
    """Separate first argument from other."""

    def _wrapper(arg_1: A1) -> Callable[P, AResult]:
        def _func(*args: P.args, **kwargs: P.kwargs) -> AResult:
            return func(arg_1, *args, **kwargs)

        return _func

    return _wrapper


def hof_3(func: Callable[[A, B, C], D]):
    def _wrapper(a: A, b: B) -> Callable[[C], D]:
        return lambda c: func(a, b, c)

    return _wrapper


def hof_4(func: Callable[[A, B, C, D], E]):
    def _wrapper(a: A, b: B, c: C) -> Callable[[D], E]:
        return lambda d: func(a, b, c, d)

    return _wrapper


def hof_5(func: Callable[[A, B, C, D, E], F]):
    def _wrapper(a: A, b: B, c: C, d: D) -> Callable[[E], F]:
        return lambda e: func(a, b, c, d, e)

    return _wrapper


@hof_3
def creducel(folder: Callable[[A, B], A], initial: A, lst: Iterable[B]):
    return reduce(folder, lst, initial)


@hof_3
def creducer(folder: Callable[[A, B], B], initial: B, lst: Iterable[A]):
    return reduce(lambda x, y: folder(y, x), lst[::-1], initial)


@hof_2
def cmap(mapper: Callable[[A], B], lst: Iterable[A]) -> Iterable[B]:
    return map(mapper, lst)


@hof_2
def cfilter(predicate: Callable[[A], bool], lst: Iterable[A]) -> Iterable[A]:
    return filter(predicate, lst)
