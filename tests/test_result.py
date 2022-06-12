import pytest

from pymon.result import EmptyChooseOkError, FailedChooseOkError, choose_ok


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
