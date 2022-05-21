from typing import SupportsIndex

from pymon.core import hof2


@hof2
def center(length: SupportsIndex, fillchar: bytes, arg: bytes) -> bytes:
    """Point-free version of `bytes.center`.

    Args:
        length (SupportsIndex): of result bytestring.
        fillchar (bytes): to fill `bytes` around.
        arg (bytes): to centralize.
    """
    return arg.center(length, fillchar)
