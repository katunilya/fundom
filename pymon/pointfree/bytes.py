from typing import SupportsIndex

from pymon.core import hof2, hof3


@hof2
def center(length: SupportsIndex, fillchar: bytes, arg: bytes) -> bytes:
    """Point-free version of `bytes.center`.

    Args:
        length (SupportsIndex): of result bytestring.
        fillchar (bytes): to fill `bytes` around.
        arg (bytes): to centralize.
    """
    return arg.center(length, fillchar)


@hof3
def count(sub: bytes, arg: bytes) -> int:
    """Point-free version of `bytes.count`.

    Args:
        sub (bytes): substring to count.
        arg (bytes): to count in.

    Returns:
        int: number of occurances of `pattern` in `arg`.
    """
    return arg.count(sub)
