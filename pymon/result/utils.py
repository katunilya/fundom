from pymon.core import hof1
from pymon.result.core import safe


@hof1
@safe
def str_to_bytes(encoding: str, data: str) -> bytes:
    """Safely convert `str` to `bytes`.

    Args:
        encoding (str): to convert with.
        data (str): to convert.

    Returns:
        bytes: result.
    """
    return data.encode(encoding)


@hof1
@safe
def bytes_to_str(encoding: str, data: bytes) -> str:
    """Safely convert `bytes` to `str`.

    Args:
        encoding (str): to convert with.
        data (bytes): to convert.

    Returns:
        str: result.
    """
    return data.decode(encoding)


str_to_bytes_utf_8 = str_to_bytes("UTF-8")
bytes_to_str_utf_8 = bytes_to_str("UTF-8")
