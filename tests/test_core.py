from pymon.core import Func


def test_func():
    f = Func(lambda x: x + 1)

    g = f << (lambda x: x + 3) << (lambda x: x**2)

    assert g(5) == 81
