from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from functools import reduce, wraps
from typing import Any, Awaitable, Callable, Generator, Generic, Iterable, TypeVar

T = TypeVar("T")
V = TypeVar("V")
U = TypeVar("U")


@dataclass(frozen=True, slots=True)
class MonadContainer(Generic[T], ABC):
    value: T


@dataclass(slots=True, frozen=True)
class AsyncComposition(MonadContainer[Callable[[T], Awaitable[V]]]):
    def __call__(self, arg: T) -> Awaitable[V]:
        return self.value(arg)

    def __chain(self, func: Callable[[V], U]) -> Callable[[T], Awaitable[U]]:
        async def ___chain(arg: T) -> Awaitable[U]:
            return func(await self(arg))

        return ___chain

    def chain(self, func: Callable[[V], U]) -> AsyncComposition[T, U]:
        return AsyncComposition(self.__chain(func))

    def __chain_async(
        self, func: Callable[[V], Awaitable[U]]
    ) -> Callable[[T], Awaitable[U]]:
        async def ___chain_async(arg: T) -> Awaitable[U]:
            return await func(await self(arg))

        return ___chain_async

    def chain_async(self, func: Callable[[V], Awaitable[U]]) -> AsyncComposition[T, U]:
        return AsyncComposition(self.__chain_async(func))


@dataclass(slots=True, frozen=True)
class Composition(MonadContainer[Callable[[T], V]]):
    def __call__(self, arg: T) -> V:
        return self.value(arg)

    def chain(self, func: Callable[[V], U]) -> Composition[T, U]:
        return Composition(lambda t: func(self(t)))

    def chain_async(self, func: Callable[[V], Awaitable[U]]) -> AsyncComposition[T, U]:
        return AsyncComposition(lambda t: func(self(t)))


def composable(func: Callable[[T], V]) -> Composition[T, V]:
    return Composition(func)


def async_composable(func: Callable[[T], Awaitable[V]]) -> AsyncComposition[T, V]:
    return AsyncComposition(func)


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


def returns_future(func: Callable[..., T]):
    @wraps(func)
    def wrapper(*args, **kwargs) -> Future[T]:
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


# identity utils


@composable
def this(x: T) -> T:
    return x


@async_composable
async def this_async(x: T) -> T:
    return x


@composable
def returns(x: T) -> Callable[[Any], T]:
    return lambda _: x


@async_composable
def returns_async(x: T) -> Callable[[Any], Future[T]]:
    async def _returns_async(_) -> T:
        return x

    return _returns_async


# curring utils
# TODO improve annotations for HOFs

A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")
D = TypeVar("D")
E = TypeVar("E")
F = TypeVar("F")


def hof_2(func: Callable[[A, B], C]):
    def _wrapper(a: A) -> Callable[[B], C]:
        return lambda b: func(a, b)

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


def composable_hof_2(func: Callable[[A, B], C]):
    def _wrapper(a: A):
        return composable(lambda b: func(a, b))

    return _wrapper


def composable_hof_3(func: Callable[[A, B, C], D]):
    def _wrapper(a: A, b: B):
        return composable(lambda c: func(a, b, c))

    return _wrapper


def composable_hof_4(func: Callable[[A, B, C, D], E]):
    def _wrapper(a: A, b: B, c: C):
        return composable(lambda d: func(a, b, c, d))

    return _wrapper


def composable_hof_5(func: Callable[[A, B, C, D, E], F]):
    def _wrapper(a: A, b: B, c: C, d: D):
        return composable(lambda e: func(a, b, c, d, e))

    return _wrapper


def async_composable_hof_2(func: Callable[[A, B], C]):
    def _wrapper(a: A):
        return async_composable(lambda b: func(a, b))

    return _wrapper


def async_composable_hof_3(func: Callable[[A, B, C], D]):
    def _wrapper(a: A, b: B):
        return async_composable(lambda c: func(a, b, c))

    return _wrapper


def async_composable_hof_4(func: Callable[[A, B, C, D], E]):
    def _wrapper(a: A, b: B, c: C):
        return async_composable(lambda d: func(a, b, c, d))

    return _wrapper


def async_composable_hof_5(func: Callable[[A, B, C, D, E], F]):
    def _wrapper(a: A, b: B, c: C, d: D):
        return async_composable(lambda e: func(a, b, c, d, e))

    return _wrapper


@composable_hof_3
def creducel(folder: Callable[[A, B], A], initial: A, lst: Iterable[B]):
    return reduce(folder, lst, initial)


@composable_hof_3
def creducer(folder: Callable[[A, B], B], initial: B, lst: Iterable[A]):
    return reduce(lambda x, y: folder(y, x), lst[::-1], initial)


@composable_hof_2
def cmap(mapper: Callable[[A], B], lst: Iterable[A]) -> Iterable[B]:
    return map(mapper, lst)


@composable_hof_2
def cfilter(predicate: Callable[[A], bool], lst: Iterable[A]) -> Iterable[A]:
    return filter(predicate, lst)
