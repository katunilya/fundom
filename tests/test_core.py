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
