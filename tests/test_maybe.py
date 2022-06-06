import pytest

from pymon.maybe import if_some_returns


@pytest.mark.parametrize(
    "replacement, value, result",
    [
        (True, 1, True),
        (True, None, None),
    ],
)
def test_if_some_returns(replacement, value, result):
    assert if_some_returns(replacement)(value) == result
