from typing import SupportsIndex

from pymon.core import hof1, hof2, hof3
from pymon.result import safe


@hof2
def center(length: SupportsIndex, fillchar: str, arg: str) -> str:
    """Point-free version of `str.center`.

    Args:
        length (SupportsIndex): of result string.
        fillchar (str): to fill `str` around.
        arg (str): to centralize.
    """
    return arg.center(length, fillchar)


@hof3
def count(sub: str, arg: str) -> int:
    """Point-free version of `str.count`.

    Args:
        sub (str): substring to count.
        arg (str): to count in.

    Returns:
        int: number of occurances of `pattern` in `arg`.
    """
    return arg.count(sub)


@hof1
@safe
def encode(encoding: str, arg: str) -> bytes:
    """Point-free version of `str.encode`.

    Args:
        encoding (str): to encode with.
        arg (str): to encode.

    Returns:
        bytes | Exception: result
    """
    return arg.encode(encoding)
