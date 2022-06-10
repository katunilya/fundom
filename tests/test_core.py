import pytest

from pymon.core import compose, future, this_future


def test_func():
    f = compose(lambda x: x + 1)

    g = f << (lambda x: x + 3) << (lambda x: x**2)

    assert g(5) == 81


def add1(x: int):
    return x + 1


def add3(x: int):
    return x + 3


def power2(x: int):
    return x**2


def minus5(x: int):
    return future(this_future(x - 5))


@pytest.mark.asyncio
async def test_compose():
    f = compose() << add1 << add3 << power2 >> minus5
    assert await f(5) == 76
