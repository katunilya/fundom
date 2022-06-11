import pytest

from pymon.core import compose


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
