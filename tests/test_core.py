import pytest

from pymon.core import Func, func, future, this_async


def test_func():
    f = Func(lambda x: x + 1)

    g = f << (lambda x: x + 3) << (lambda x: x**2)

    assert g(5) == 81


def add1(x: int):
    return x + 1


def add3(x: int):
    return x + 3


def power2(x: int):
    return x**2


def minus5(x: int):
    return future(this_async(x - 5))


@pytest.mark.asyncio
async def test_func_decorator():
    f = func(add1) << add3 << power2 >> minus5
    assert await f(5) == 76
