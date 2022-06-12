from typing import SupportsIndex

from fundom.core import hof1, hof2, hof3
from fundom.result import safe


@hof2
def center(length: SupportsIndex, fill_char: bytes, arg: bytes) -> bytes:
    """Point-free version of `bytes.center`.

    Args:
        length (SupportsIndex): of result bytestring.
        fill_char (bytes): to fill `bytes` around.
        arg (bytes): to centralize.
    """
    return arg.center(length, fill_char)


@hof3
def count(sub: bytes, arg: bytes) -> int:
    """Point-free version of `bytes.count`.

    Args:
        sub (bytes): substring to count.
        arg (bytes): to count in.

    Returns:
        int: number of occurrences of `pattern` in `arg`.
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
        sub (bytes): to search.
        arg (bytes): to search int.

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
def index(sub: bytes, arg: bytes) -> int:
    """Point-free version of `bytes.index`.

    Args:
        sub (bytes): to search.
        arg (bytes): to search in.

    Returns:
        int: lowest index in arg where `sub` is found. Raises error if nothing found.
    """
    return arg.index(sub)


@hof1
def removeprefix(prefix: bytes, arg: bytes) -> bytes:
    """Point-free version of `bytes.removeprefix`.

    Args:
        prefix (bytes): to remove.
        arg (bytes): to remove from.

    Returns:
        bytes: without prefix if it is possible.
    """
    return arg.removeprefix(prefix)


@hof1
def removesuffix(suffix: bytes, arg: bytes) -> bytes:
    """Point-free version of `bytes.removesuffix`.

    Args:
        suffix (bytes): to remove.
        arg (bytes): to remove from.

    Returns:
        bytes: without suffix if it is possible.
    """
    return arg.removesuffix(suffix)


@hof2
def replace(old: bytes, new: bytes, arg: bytes) -> bytes:
    """Point-free version of `bytes.replace`.

    Args:
        old (bytes): to replace.
        new (bytes): to replace with.
        arg (bytes): to replace in.

    Returns:
        bytes: result.
    """
    return arg.replace(old, new)


@hof1
def split(sep: bytes, arg: bytes) -> list[bytes]:
    """Point-free version of `bytes.split`.

    Args:
        sep (bytes): to split with.
        arg (bytes): to split.

    Returns:
        list[bytes]: result of split.
    """
    return arg.split(sep)


@hof1
def startswith(sub: bytes, arg: bytes) -> bool:
    """Point-free version of `bytes.startswith`.

    Args:
        sub (bytes): substring to check.
        arg (bytes): to check in.

    Returns:
        bool: if `arg` starts with `sub`.
    """
    return arg.startswith(sub)


@hof1
def strip(chars: bytes, arg: bytes) -> bytes:
    """Point-free version of `bytes.strip`.

    Args:
        chars (bytes): to strip.
        arg (bytes): to strip from.

    Returns:
        bytes: result.
    """
    return arg.strip(chars)
