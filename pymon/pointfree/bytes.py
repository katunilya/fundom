from typing import SupportsIndex

from pymon.core import hof1, hof2, hof3
from pymon.result.core import safe


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


@hof1
@safe
def decode(encoding: str, arg: bytes) -> str:
    """Point-free version of `bytes.decode`.

    Args:
        encoding (str): to decode with.
        arg (bytes): to decode.

    Returns:
        str | Exception: result.
    """
    return arg.decode(encoding)


@hof1
def endswith(sub: bytes, arg: bytes) -> bool:
    """Point-free version of `bytes.endswith`.

    Args:
        sub (bytes): substring to check.
        arg (bytes): to check in.

    Returns:
        bool: if `arg` endswith `sub`.
    """
    return arg.endswith(sub)


def find(sub: bytes, arg: bytes) -> int | None:
    """Point-free maybe version of `bytes.find`.

    Args:
        sub (bytes): to serach.
        arg (bytes): to search int.

    Returns:
        int | None: lowest index in arg where sub is found. `None` if nothing found.
    """
    match arg.find(sub):
        case -1:
            return None
        case some:
            return some
