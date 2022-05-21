from typing import SupportsIndex

from pymon.core import hof1, hof2, hof3
from pymon.result import safe


@hof2
def center(length: SupportsIndex, fillchar: str, arg: str) -> str:
    """Point-free version of `str.center`.

    Return a centered string of length width. Padding is done using the specified fill
    character (default is a space).

    Args:
        length (SupportsIndex): of result string.
        fillchar (str): to fill `str`  around.
        arg (str): to centralize.
    """
    return arg.center(length, fillchar)


@hof3
def count(pattern: str, start: SupportsIndex, end: SupportsIndex, arg: str) -> int:
    """Point-free version of `str.count`.

    Return the number of non-overlapping occurrences of substring sub in string
    S[start:end]. Optional arguments start and end are interpreted as in slice notation.

    Args:
        pattern (str): what to count.
        start (SupportsIndex): where to start (as slice).
        end (SupportsIndex): where to end (as slice).
        arg (str): to count in.

    Returns:
        int: number of occurances of `pattern` in `arg`.
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
