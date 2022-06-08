from typing import Iterable, SupportsIndex

from pymon.core import hof1, hof2, hof3
from pymon.result import safe


@hof2
def center(length: SupportsIndex, fill_char: str, arg: str) -> str:
    """Point-free version of `str.center`.

    Args:
        length (SupportsIndex): of result string.
        fill_char (str): to fill `str` around.
        arg (str): to centralize.
    """
    return arg.center(length, fill_char)


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


@hof1
def endswith(sub: str, arg: str) -> bool:
    """Point-free version of `str.endswith`.

    Args:
        sub (str): substring to check.
        arg (str): to check in.

    Returns:
        bool: if `arg` endswith `sub`.
    """
    return arg.endswith(sub)


def find(sub: str, arg: str) -> int | None:
    """Point-free maybe version of `str.find`.

    Args:
        sub (str): to serach.
        arg (str): to search int.

    Returns:
        int | None: lowest index in arg where sub is found. `None` if nothing found.
    """
    match arg.find(sub):
        case -1:
            return None
        case some:
            return some


@hof1
@safe
def index(sub: str, arg: str) -> int:
    """Point-free version of `str.index`.

    Args:
        sub (str): to search.
        arg (str): to search in.

    Returns:
        int: lowest index in arg where `sub` is found. Raises error if nothing found.
    """
    return arg.index(sub)


@hof1
def join_by(concatenator: str, arg: Iterable[str]) -> str:
    """Join incoming `Iterable[str]` by some `concatenatror`.

    Args:
        concatenator (str): to join with.
        arg (Iterable[str]): to be joined.

    Returns:
        str: joined string.
    """
    return concatenator.join(arg)


@hof1
def join(iterable: Iterable[str], arg: str) -> str:
    """Point-free version of `str.join`.

    Args:
        iterable (Iterable[str]): to join.
        arg (str): to join with.

    Returns:
        str: joined string.
    """
    return arg.join(iterable)


@hof1
def removeprefix(prefix: str, arg: str) -> str:
    """Point-free version of `str.removeprefix`.

    Args:
        prefix (str): to remove.
        arg (str): to remove from.

    Returns:
        str: if the string starts with the prefix string, return string[len(prefix):].
        Otherwise, return a copy of the original string:
    """
    return arg.removeprefix(prefix)


@hof1
def removesuffix(suffix: str, arg: str) -> str:
    """Point-free version of `str.removesuffix`.

    Args:
        suffix (str): to remove.
        arg (str): to remove from.

    Returns:
        str: If the string ends with the suffix string and that suffix is not empty,
        return string[:-len(suffix)]. Otherwise, return a copy of the original string:
    """
    return arg.removesuffix(suffix)


@hof2
def replace(old: str, new: str, arg: str) -> str:
    """Point-free version of `str.replace`.

    Args:
        old (str): to replace.
        new (str): to replace with.
        arg (str): to replace in.

    Returns:
        str: result.
    """
    return arg.replace(old, new)


@hof1
def split(sep: str, arg: str) -> list[str]:
    """Point-free version of `str.split`.

    Args:
        sep (str): to split with.
        arg (str): to split.

    Returns:
        list[str]: result of split.
    """
    return arg.split(sep)


@hof1
def startswith(sub: str, arg: str) -> bool:
    """Point-free version of `str.startswith`.

    Args:
        sub (str): substring to check.
        arg (str): to check in.

    Returns:
        bool: if `arg` starts with `sub`.
    """
    return arg.startswith(sub)


@hof1
def strip(chars: str, arg: str) -> str:
    """Point-free version of `str.strip`.

    Args:
        chars (str): to strip.
        arg (str): to strip from.

    Returns:
        str: result.
    """
    return arg.strip(chars)
