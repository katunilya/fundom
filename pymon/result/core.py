from dataclasses import dataclass
from functools import wraps
from typing import Awaitable, Callable, TypeVar

from pymon.core import Future, MonadContainer, this_async

TOk = TypeVar("TOk")
TFail = TypeVar("TFail")


@dataclass(frozen=True, slots=True)
class Ok(MonadContainer[TOk]):
    ...


@dataclass(frozen=True, slots=True)
class Fail(MonadContainer[TFail]):
    ...


Result = Ok[TOk] | Fail[TFail]
Safe = Ok[TOk] | Fail[Exception]


def safe_unit(value: TOk | Exception) -> Safe[TOk]:
    match value:
        case Exception():
            return Fail(Exception)
        case _:
            return Ok(value)


# bindings
VOk = TypeVar("VOk")
VFail = TypeVar("VFail")


def if_ok(func: Callable[[TOk], Result[VOk, VFail]]):
    @wraps(func)
    def _wrapper(arg: Result[TOk, TFail]):
        match arg:
            case Ok(value):
                return func(value)
            case Fail() as fail:
                return fail

    return _wrapper


def if_ok_async(func: Callable[[TOk], Awaitable[Result[VOk, VFail]]]):
    @wraps(func)
    def _wrapper(arg: Result[TOk, TFail]):
        match arg:
            case Ok(value):
                return Future(func(value))
            case Fail() as fail:
                return Future(this_async(fail))

    return _wrapper


def if_fail(func: Callable[[TOk], Result[VOk, VFail]]):
    @wraps(func)
    def _wrapper(arg: Result[TOk, TFail]):
        match arg:
            case Ok(value):
                return func(value)
            case Fail() as fail:
                return fail

    return _wrapper


def if_fail_async(func: Callable[[TOk], Awaitable[Result[VOk, VFail]]]):
    @wraps(func)
    def _wrapper(arg: Result[TOk, TFail]):
        match arg:
            case Ok(value):
                return Future(func(value))
            case Fail() as fail:
                return Future(this_async(fail))

    return _wrapper


def safe(func: Callable[[TOk], VOk]) -> Callable[[TOk], Safe[VOk]]:
    @wraps(func)
    def _wrapper(arg: TOk) -> Safe[VOk]:
        try:
            return Ok(func(arg))
        except Exception as err:
            return Fail(err)

    return _wrapper


def async_safe(
    func: Callable[[TOk], Awaitable[VOk]]
) -> Callable[[TOk], Future[Safe[VOk]]]:
    async def __executor(arg: TOk) -> Safe[VOk]:
        try:
            return Ok(await func(arg))
        except Exception as err:
            return Fail(err)

    @wraps(func)
    def _wrapper(arg: TOk) -> Future[Safe[VOk]]:
        return Future(__executor(arg))

    return _wrapper
