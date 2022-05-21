from typing import Callable, SupportsIndex


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
    return lambda data: data.count(pattern, start, end)
