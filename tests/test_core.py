import inspect

import pytest

from fundom.core import (
    compose,
    future,
    pipe,
    returns,
    returns_future,
    this,
    this_future,
)


@pytest.mark.parametrize(
    "funcs, arg, result",
    [
        ([(lambda x: x + 1)], 3, 4),
        ([(lambda x: x + 1), (lambda x: x**2)], 3, 16),
        ([(lambda x: x > 3)], 1, False),
    ],
)
def test_compose_sync_only(funcs, arg, result):
    c = compose()
    for func in funcs:
        c = c << func

    assert c(arg) == result


async def add_1(x: int) -> int:
    return x + 1


async def power_2(x: int) -> int:
    return x**2


async def more_then_3(x: int) -> bool:
    return x > 3


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "funcs, arg, result",
    [
        ([add_1], 3, 4),
        ([add_1, power_2], 3, 16),
        ([more_then_3], 1, False),
    ],
)
async def test_compose_async_only(funcs, arg, result):
    c = compose()
    for func in funcs:
        c = c >> func

    assert await c(arg) == result


@pytest.mark.asyncio
async def test_compose_sync_async():
    f = (
        compose()
        << (lambda x: x + 1)
        << (lambda x: x**2)
        >> add_1
        >> more_then_3
        << (lambda t: not t)
    )
    assert await f(3) is False


async def async_identity(x):
    return x


@pytest.mark.asyncio
async def test_future():
    fv = future(async_identity(3))

    assert inspect.isawaitable(fv)
    assert await fv == 3


@pytest.mark.asyncio
async def test_future_returns():
    async_identity_future = future.returns(async_identity)

    fv = async_identity_future(3)

    assert inspect.isawaitable(fv)
    assert await fv == 3


@pytest.mark.asyncio
async def test_future_lshift():
    fv = future(async_identity(3)) << (lambda x: x + 1)

    assert inspect.isawaitable(fv)
    assert await fv == 4


@pytest.mark.asyncio
async def test_future_rshift():
    fv = future(async_identity(3)) >> add_1

    assert inspect.isawaitable(fv)
    assert await fv == 4


def test_pipe_lshift():
    pl = pipe(3) << (lambda x: x + 3)

    assert isinstance(pl, pipe)
    assert pl.value == 6


@pytest.mark.asyncio
async def test_pipe_rshift():
    pl = pipe(3) >> add_1

    assert isinstance(pl, future)
    assert await pl == 4


def test_pipe_finish():
    pl = pipe(3) << (lambda x: x + 3)
    assert pl.finish() == 6


def test_pipe_returns():
    f = pipe.returns(lambda x: pipe(x) >> (lambda x: x + 3))
    assert f(3) == 6


@pytest.mark.parametrize("arg", [{}, 1, 2, -1, "hello"])
def test_this(arg):
    assert this(arg) == arg


@pytest.mark.asyncio
@pytest.mark.parametrize("arg", [{}, 1, 2, -1, "hello"])
async def test_this_future(arg):
    fv = this_future(arg)

    assert inspect.isawaitable(fv)
    assert isinstance(fv, future)
    assert await fv == arg


@pytest.mark.parametrize("arg", [{}, 1, 2, -1, "hello"])
def test_returns(arg):
    r = returns(arg)
    assert r() == arg
    assert r(arg) == arg
    assert r(some="wow") == arg
    assert r(5, 3, 2) == arg


@pytest.mark.asyncio
@pytest.mark.parametrize("arg", [{}, 1, 2, -1, "hello"])
async def test_returns_future(arg):
    r = returns_future(arg)

    for fv in [r(), r(arg), r(some="wow"), r(5, 3, 2)]:
        assert inspect.isawaitable(fv)
        assert isinstance(fv, future)
        assert await fv == arg
