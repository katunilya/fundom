from typing import Callable, SupportsIndex


def center(width: SupportsIndex, fillchar: str = " ") -> Callable[[str], str]:
    """Point-free version of `str.center`.

    Return a centered string of length width. Padding is done using the specified fill
    character (default is a space).
    """
    return lambda data: data.center(width, fillchar)
