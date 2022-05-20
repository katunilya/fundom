# Utils

> Auto-generated documentation for [pymon.result.utils](https://github.com/katunilya/pymon/blob/main/pymon/result/utils.py) module.

- [Pymon](../../README.md#pymon-index) / [Modules](../../MODULES.md#pymon-modules) / [Pymon](../index.md#pymon) / [Result](index.md#result) / Utils
    - [bytes_to_str](#bytes_to_str)
    - [str_to_bytes](#str_to_bytes)

## bytes_to_str

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result/utils.py#L20)

```python
@hof1
@safe
def bytes_to_str(encoding: str, data: bytes) -> str:
```

Safely convert `bytes` to `str`.

#### Arguments

- `encoding` *str* - to convert with.
- `data` *bytes* - to convert.

#### Returns

- `str` - result.

#### See also

- [hof1](../core.md#hof1)
- [safe](core.md#safe)

## str_to_bytes

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result/utils.py#L5)

```python
@hof1
@safe
def str_to_bytes(encoding: str, data: str) -> bytes:
```

Safely convert `str` to `bytes`.

#### Arguments

- `encoding` *str* - to convert with.
- `data` *str* - to convert.

#### Returns

- `bytes` - result.

#### See also

- [hof1](../core.md#hof1)
- [safe](core.md#safe)
