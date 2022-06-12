import pytest

from pymon.result import (
    EmptyChooseOkError,
    FailedChooseOkError,
    choose_ok,
    choose_ok_future,
)


@pytest.mark.parametrize(
    "value, funcs, result",
    [
        (3, [lambda x: x + 1, lambda x: x + 2], 4),
        (3, [lambda x: x + 2, lambda x: x + 1], 5),
        (3, [lambda x: x + 2, lambda _: Exception()], 5),
        (3, [lambda _: Exception(), lambda x: x + 2], 5),
    ],
)
def test_choose(value, funcs, result):
    c = choose_ok()

    for func in funcs:
        c = c | func

    assert c(value) == result


def test_choose_ok_returns_error_on_empty():
    c = choose_ok()
    assert isinstance(c(None), EmptyChooseOkError)


def test_choose_ok_returns_error_on_failed():
    c = (
        choose_ok()
        | (lambda x: x if x < 3 else Exception())
        | (lambda x: x if x > 10 else Exception())
    )
    result = c(6)
    assert isinstance(result, FailedChooseOkError)
    assert result.args == (6,)


async def add_1(x: int) -> int:
    return x + 1


async def add_2(x: int) -> int:
    return x + 2


async def exc(_) -> Exception:
    return Exception()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "value, funcs, result",
    [
        (3, [add_1, add_2], 4),
        (3, [add_2, add_1], 5),
        (3, [add_2, exc], 5),
        (3, [exc, add_2], 5),
    ],
)
async def test_choose_ok_future(value, funcs, result):
    c = choose_ok_future()

    for func in funcs:
        c = c | func

    assert await c(value) == result


@pytest.mark.asyncio
async def test_choose_ok_future_returns_error_on_empty():
    c = choose_ok_future()
    assert isinstance(await c(None), EmptyChooseOkError)


async def less_then_3(x: int) -> int | Exception:
    return x if x < 3 else Exception()


async def more_then_10(x: int) -> int | Exception:
    return x if x > 10 else Exception()


@pytest.mark.asyncio
async def test_choose_ok_future_returns_error_on_failed():
    c = choose_ok_future() | less_then_3 | more_then_10

    result = await c(6)
    assert isinstance(result, FailedChooseOkError)
    assert result.args == (6,)
