from __future__ import annotations

from dataclasses import dataclass
from functools import reduce, wraps
from typing import (
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


@dataclass(slots=True, frozen=True)
class Future(Generic[T]):
    """Abstraction over awaitable value to run in pipeline.

    Example::
            result = await (
                Future(get_user_async)
                << if_role_is("moderator")
                << set_role("admin")
                >> update_user_async
            )
    """

    value: Awaitable[T]

    def __await__(self) -> Generator[None, None, T]:
        return self.value.__await__()

    async def __then(self, func: Callable[[T], V]) -> V:
        return func(await self.value)

    def then(self, func: Callable[[T], V]) -> Future[V]:
        """Execute sync `func` next on awaited internal value.

        Args:
            func (Callable[[T], V]): to execute.

        Returns:
            Future[V]: awaitable result of execution.
        """
        return Future(self.__then(func))

    async def __then_async(self, func: Callable[[T], Awaitable[V]]) -> V:
        return await func(await self.value)

    def then_async(self, func: Callable[[T], Awaitable[V]]) -> Future[V]:
        """Execute async `func` next on awaited internal value.

        Args:
            func (Callable[[T], Awaitable[V]]): to execute.

        Returns:
            Future[V]: awaitable result of execution.
        """
        return Future(self.__then_async(func))

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
class Pipe(Generic[T]):
    """Abstraction over some value to run in pipeline.

    Example::
            result: int = (
                Pipe(12)
                << (lambda x: x + 1)
                << (lambda x: x**2)
                << (lambda x: x // 3)
            ).finish()
    """

    value: T

    def then(self, func: Callable[[T], V]) -> Pipe[V]:
        """Execute sync `func` next on internal value.

        Args:
            func (Callable[[T], V]): to execute.

        Returns:
            Pipe[V]: execution result.
        """
        return Pipe(func(self.value))

    def then_async(self, func: Callable[[T], Awaitable[V]]) -> Future[V]:
        """Execute async `func` next on internal value.

        Returns `Future` for further pipeline.

        Args:
            func (Callable[[T], Awaitable[V]]): to execute.

        Returns:
            Future[V]: execution result.
        """
        return Future(func(self.value))

    def __lshift__(self, func: Callable[[T], V]) -> Pipe[V]:
        return self.then(func)

    def __rshift__(self, func: Callable[[T], Awaitable[V]]) -> Future[V]:
        return self.then_async(func)

    def finish(self) -> T:
        """Finish `Pipe` by unpacking internal value.

        Returns:
            T: internal value
        """
        return self.value


def pipeline(func: Callable[P, Pipe[T]]) -> Callable[P, T]:
    """Decorator for functions that return `Pipe` object for seamless unwrapping."""

    @wraps(func)
    def _wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        return func(*args, **kwargs).value

    return _wrapper


# identity utils


def this(x: T) -> T:
    """Syncronous identity function."""
    return x


async def this_async(x: T) -> T:
    """Asynchronous identity function."""
    return x


def returns(x: T) -> Callable[P, T]:
    """Return `T` on any input."""

    def _returns(*_: P.args, **__: P.kwargs) -> T:
        return x

    return _returns


def returns_async(x: T) -> Callable[P, Future[T]]:
    """Return awaitable `T` on any input."""

    async def _returns_async(*_: P.args, **__: P.kwargs) -> T:
        return x

    return _returns_async


# curring utils

A1 = TypeVar("A1")
A2 = TypeVar("A2")
A3 = TypeVar("A3")
AResult = TypeVar("AResult")


def hof1(func: Callable[Concatenate[A1, P], AResult]):
    """Separate first argument from other."""

    def _wrapper(arg_1: A1) -> Callable[P, AResult]:
        def _func(*args: P.args, **kwargs: P.kwargs) -> AResult:
            return func(arg_1, *args, **kwargs)

        return _func

    return _wrapper


def hof2(func: Callable[Concatenate[A1, A2, P], AResult]):
    """Separate first 2 arguments from other."""

    def _wrapper(arg_1: A1, arg_2: A2) -> Callable[P, AResult]:
        def _func(*args: P.args, **kwargs: P.kwargs) -> AResult:
            return func(arg_1, arg_2, *args, **kwargs)

        return _func

    return _wrapper


def hof3(func: Callable[Concatenate[A1, A2, A3, P], AResult]):
    """Separate first 3 arguments from other."""

    def _wrapper(arg_1: A1, arg_2: A2, arg_3: A3) -> Callable[P, AResult]:
        def _func(*args: P.args, **kwargs: P.kwargs) -> AResult:
            return func(arg_1, arg_2, arg_3, *args, **kwargs)

        return _func

    return _wrapper


@hof2
def creducel(folder: Callable[[A1, A2], A1], initial: A1, lst: Iterable[A2]) -> A1:
    """Curried `reduce` left function.

    Args:
        folder (Callable[[A1, A2], A1]): aggregator.
        initial (A1): initial aggregation value.
        lst (Iterable[A2]): data to reduce.

    Returns:
        A1: reduction result.
    """
    return reduce(folder, lst, initial)


@hof2
def creducer(folder: Callable[[A1, A2], A2], initial: A2, lst: Iterable[A1]) -> A2:
    """Curried `reduce` right function.

    Args:
        folder (Callable[[A1, A2], A2]): aggregator.
        initial (A2): initial aggregation value.
        lst (Iterable[A1]): data to reduce.

    Returns:
        A2: reduction result.
    """
    return reduce(lambda x, y: folder(y, x), lst[::-1], initial)


@hof1
def cmap(mapper: Callable[[A1], A2], lst: Iterable[A1]) -> Iterable[A2]:
    """Curreid `map` function.

    Args:
        mapper (Callable[[A1], A2]): mapper for element of iterable.
        lst (Iterable[A1]): to map.

    Returns:
        Iterable[A2]: map result.
    """
    return map(mapper, lst)


@hof1
def cfilter(predicate: Callable[[A1], bool], lst: Iterable[A1]) -> Iterable[A1]:
    """Curried `filter` function.

    Args:
        predicate (Callable[[A1], bool]): to filter with.
        lst (Iterable[A1]): to filter.

    Returns:
        Iterable[A1]: filtered iterable.
    """
    return filter(predicate, lst)
