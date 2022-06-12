import pytest

from pymon.maybe import choose_some, if_some_returns


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
    "value, funcs, result",
    [
        (3, [lambda x: x + 1, lambda x: x + 2], 4),
        (3, [lambda x: x + 2, lambda x: x + 1], 5),
        (3, [lambda x: x + 2, lambda _: None], 5),
        (3, [lambda _: None, lambda x: x + 2], 5),
    ],
)
def test_choose(value, funcs, result):
    c = choose_some()

    for func in funcs:
        c = c | func

    assert c(value) == result


def test_choose_some_returns_error_on_empty():
    c = choose_some()
    assert c(1) is None


def test_choose_some_returns_error_on_failed():
    c = (
        choose_some()
        | (lambda x: x if x < 3 else None)
        | (lambda x: x if x > 10 else None)
    )
    assert c(6) is None
