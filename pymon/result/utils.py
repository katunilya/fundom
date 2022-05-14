from pymon.result.core import safe


def str_to_bytes(encoding: str):
    @safe
    def _str_to_bytes(data: str):
        return data.encode(encoding)

    return _str_to_bytes


def bytes_to_str(encoding: str):
    @safe
    def _bytes_to_str(data: bytes):
        return data.decode(encoding)

    return _bytes_to_str


str_to_bytes_utf_8 = str_to_bytes("UTF-8")
bytes_to_str_utf_8 = bytes_to_str("UTF-8")
