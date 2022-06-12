import pytest

from pymon.predicate import each


@pytest.mark.parametrize(
    "predicates, arg, result",
    [
        ([(lambda x: x > 3)], 5, True),
        ([(lambda x: x > 3), (lambda x: x < 10)], 20, False),
    ],
)
def test_each_sync_only(predicates, arg, result):
    e = each()
    for predicate in predicates:
        e = e << predicate

    assert e(arg) == result


async def more_than_3(x: int) -> bool:
    return x > 3


async def less_than_10(x: int) -> bool:
    return x < 10


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "predicates, arg, result",
    [
        ([more_than_3], 5, True),
        ([more_than_3, less_than_10], 20, False),
    ],
)
async def test_each_async_only(predicates, arg, result):
    e = each()
    for predicate in predicates:
        e = e >> predicate

    assert await e(arg) == result


@pytest.mark.asyncio
async def test_each_sync_and_async():
    e = each() << (lambda x: x % 2 == 0) >> (more_than_3) >> (less_than_10)

    assert await e(6) is True
    assert await e(7) is False
    assert await e(15) is False
