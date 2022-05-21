from typing import Callable, SupportsIndex

from pymon.core import hof3


def center(width: SupportsIndex, fillchar: str = " ") -> Callable[[str], str]:
    """Point-free version of `str.center`.

    Return a centered string of length width. Padding is done using the specified fill
    character (default is a space).
    """
    return lambda data: data.center(width, fillchar)


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
