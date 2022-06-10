from __future__ import annotations

from dataclasses import dataclass
from functools import reduce, wraps
from typing import (
    Any,
    Awaitable,
    Callable,
    Concatenate,
    Coroutine,
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
class future(Generic[T]):  # noqa
    """Abstraction over awaitable value to run in pipeline.

    Example::

            result = await (
                future(get_user_async)
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

    async def __then_async(self, func: Callable[[T], Awaitable[V]]) -> V:
        return await func(await self.value)

    def __rshift__(self, func: Callable[[T], Awaitable[V]]) -> future[V]:
        return future(self.__then_async(func))

    def __lshift__(self, func: Callable[[T], V]) -> future[V]:
        return future(self.__then(func))

    @staticmethod
    def returns(func: Callable[P, Coroutine[Any, Any, T]]):
        """Wraps returned value of async function to `future`."""

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> future[T]:
            match func(*args, **kwargs):
                case future() as _future:
                    return _future
                case awaitable:
                    return future(awaitable)

        return wrapper


@dataclass(slots=True, frozen=True)
class pipe(Generic[T]):  # noqa
    """Abstraction over some value to run in pipeline.

    Example::

            result: int = (
                pipe(12)
                << (lambda x: x + 1)
                << (lambda x: x**2)
                << (lambda x: x // 3)
            ).finish()
    """

    value: T

    def __lshift__(self, func: Callable[[T], V]) -> pipe[V]:
        return pipe(func(self.value))

    def __rshift__(self, func: Callable[[T], Awaitable[V]]) -> future[V]:
        return future(func(self.value))

    def finish(self) -> T:
        """Finish `pipe` by unpacking internal value.

        Returns:
            T: internal value
        """
        return self.value

    @staticmethod
    def returns(func: Callable[P, pipe[T]]) -> Callable[P, T]:
        """Decorator for functions that return `pipe` object for seamless unwrapping."""

        @wraps(func)
        def _wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            return func(*args, **kwargs).value

        return _wrapper


# identity utils


def this(*args: P.args, **_: P.kwargs):
    """Synchronous identity function."""
    return args


@future.returns
async def this_future(*args: P.args, **_: P.kwargs):
    """Asynchronous identity function."""
    return args


def returns(x: T) -> Callable[P, T]:
    """Return `T` on any input."""

    def _returns(*_: P.args, **__: P.kwargs) -> T:
        return x

    return _returns


def returns_future(x: T) -> Callable[P, future[T]]:
    """Return awaitable `T` on any input."""

    @future.returns
    async def _returns_future(*_: P.args, **__: P.kwargs) -> T:
        return x

    return _returns_future


@dataclass(slots=True, frozen=True)
class FutureFunc(Generic[P, V]):
    """Abstraction over async function."""

    func: Callable[P, Awaitable[V]] = this

    def __call__(self, *args: P.args, **kwds: P.kwargs) -> future[V]:  # noqa
        return future(self.func(*args, **kwds))

    def __lshift__(self, other: Callable[[V], U]) -> FutureFunc[P, U]:
        def composition(*args: P.args, **kwargs: P.kwargs) -> U:
            return self.__call__(*args, **kwargs) << other

        return FutureFunc(composition)

    def __rshift__(self, other: Callable[[V], Awaitable[U]]) -> FutureFunc[P, U]:
        def composition(*args: P.args, **kwargs: P.kwargs) -> future[U]:
            return self.__call__(*args, **kwargs) >> other

        return FutureFunc(composition)


@dataclass(slots=True, frozen=True)
class Func(Generic[P, V]):
    """Function composition abstraction."""

    func: Callable[P, V] = this

    def __call__(self, *args: P.args, **kwds: P.kwargs) -> V:  # noqa
        return self.func(*args, **kwds)

    def __lshift__(self, other: Callable[[V], U]) -> Func[P, U]:
        def composition(*args: P.args, **kwargs: P.kwargs) -> U:
            return other(self.__call__(*args, **kwargs))

        return Func(composition)

    def __rshift__(self, other: Callable[[V], Awaitable[U]]) -> FutureFunc[P, U]:
        def composition(*args: P.args, **kwargs: P.kwargs) -> Awaitable[U]:
            return other(self.__call__(*args, **kwargs))

        return FutureFunc(composition)


def func(func: Callable[P, V]) -> Func[P, V]:
    """Decorator for making functions composable."""
    return Func(func)


def future_func(func: Callable[P, Awaitable[V]]) -> FutureFunc[P, V]:
    """Decorator for making async functions composable."""
    return FutureFunc(func)


# curring utils

A1 = TypeVar("A1")
A2 = TypeVar("A2")
A3 = TypeVar("A3")
AResult = TypeVar("AResult")


def hof1(f: Callable[Concatenate[A1, P], AResult]):
    """Separate first argument from other."""

    @wraps(f)
    def _wrapper(arg_1: A1) -> Callable[P, AResult]:
        def _func(*args: P.args, **kwargs: P.kwargs) -> AResult:
            return f(arg_1, *args, **kwargs)

        return _func

    return _wrapper


def hof2(f: Callable[Concatenate[A1, A2, P], AResult]):
    """Separate first 2 arguments from other."""

    @wraps(f)
    def _wrapper(arg_1: A1, arg_2: A2) -> Callable[P, AResult]:
        def _func(*args: P.args, **kwargs: P.kwargs) -> AResult:
            return f(arg_1, arg_2, *args, **kwargs)

        return _func

    return _wrapper


def hof3(f: Callable[Concatenate[A1, A2, A3, P], AResult]):
    """Separate first 3 arguments from other."""

    @wraps(f)
    def _wrapper(arg_1: A1, arg_2: A2, arg_3: A3) -> Callable[P, AResult]:
        def _func(*args: P.args, **kwargs: P.kwargs) -> AResult:
            return f(arg_1, arg_2, arg_3, *args, **kwargs)

        return _func

    return _wrapper


@hof2
def foldl(folder: Callable[[A1, A2], A1], initial: A1, lst: Iterable[A2]) -> A1:
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
def foldr(folder: Callable[[A1, A2], A2], initial: A2, lst: Iterable[A1]) -> A2:
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
    """Curried `map` function.

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
