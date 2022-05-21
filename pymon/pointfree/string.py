from typing import Callable, SupportsIndex

from pymon.core import hof1, hof2, hof3
from pymon.result import safe

def center(width: SupportsIndex, fillchar: str = " ") -> Callable[[str], str]:
    """Point-free version of `str.center`.

    Return a centered string of length width. Padding is done using the specified fill
    character (default is a space).
    """
    return lambda data: data.center(width, fillchar)


def count(
    pattern: str, start: SupportsIndex | None = ..., end: SupportsIndex | None = ...
) -> Callable[[str], int]:
    """Point-free version of `str.count`.

    Return the number of non-overlapping occurrences of substring sub in string
    S[start:end]. Optional arguments start and end are interpreted as in slice notation.
    """
    return arg.count(pattern, start, end)


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