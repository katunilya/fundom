import pytest

from pymon.maybe import (
    choose_some,
    choose_some_future,
    if_none,
    if_none_returns,
    if_some,
    if_some_returns,
    some_when,
    some_when_future,
)


@pytest.mark.parametrize(
    "arg, result",
    [
        (3, 3),
        (None, None),
    ],
)
def test_if_some(arg, result):
    assert if_some(lambda x: x)(arg) == result


@pytest.mark.parametrize(
    "arg, result",
    [
        (3, 3),
        (None, 10),
    ],
)
def test_if_none(arg, result):
    assert if_none(lambda _: 10)(arg) == result


@pytest.mark.parametrize(
    "replacement, value, result",
    [
        (True, 1, True),
        (True, None, None),
    ],
)
def test_if_some_returns(replacement, value, result):
    assert if_some_returns(replacement)(value) == result


@pytest.mark.parametrize(
    "replacement, value, result",
    [
        (True, 1, 1),
        (True, None, True),
    ],
)
def test_if_none_returns(replacement, value, result):
    assert if_none_returns(replacement)(value) == result


@pytest.mark.parametrize(
    "value, funcs, result",
    [
        (3, [lambda x: x + 1, lambda x: x + 2], 4),
        (3, [lambda x: x + 2, lambda x: x + 1], 5),
        (3, [lambda x: x + 2, lambda _: None], 5),
        (3, [lambda _: None, lambda x: x + 2], 5),
    ],
)
def test_choose_some(value, funcs, result):
    c = choose_some()

    for func in funcs:
        c = c | func

    assert c(value) == result


def test_choose_some_returns_none_on_empty():
    c = choose_some()
    assert c(1) is None


def test_choose_some_returns_none_on_failed():
    c = (
        choose_some()
        | (lambda x: x if x < 3 else None)
        | (lambda x: x if x > 10 else None)
    )
    assert c(6) is None


async def add_1(x: int) -> int:
    return x + 1


async def add_2(x: int) -> int:
    return x + 2


async def nothing(_) -> None:
    return None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "value, funcs, result",
    [
        (3, [add_1, add_2], 4),
        (3, [add_2, add_1], 5),
        (3, [add_2, nothing], 5),
        (3, [nothing, add_2], 5),
    ],
)
async def test_choose_some_future(value, funcs, result):
    c = choose_some_future()

    for func in funcs:
        c = c | func

    assert await c(value) == result


@pytest.mark.asyncio
async def test_choose_some_future_returns_none_on_empty():
    c = choose_some_future()
    assert await c(1) is None


async def less_than_3(x: int) -> int | None:
    return x if x < 3 else None


async def more_than_10(x: int) -> int | None:
    return x if x > 10 else None


@pytest.mark.asyncio
async def test_choose_some_future_returns_none_on_failed():
    c = choose_some_future() | less_than_3 | more_than_10
    assert await c(6) is None


def test_some_when():
    p = some_when(lambda x: x > 15)
    assert p(10) is None
    assert p(16) == 16


async def more_than_15(x: int) -> bool:
    return x > 15


@pytest.mark.asyncio
async def test_some_when_future():
    p = some_when_future(more_than_15)
    assert await p(10) is None
    assert await p(16) == 16
