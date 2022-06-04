import pytest

from pymon.result import choose_ok


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
    assert choose_ok(*funcs)(value) == result