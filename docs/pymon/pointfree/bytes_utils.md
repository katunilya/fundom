# Bytes Utils

> Auto-generated documentation for [pymon.pointfree.bytes_utils](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/bytes_utils.py) module.

- [Pymon](../../README.md#-pymon) / [Modules](../../MODULES.md#pymon-modules) / [Pymon](../index.md#pymon) / [Pointfree](index.md#pointfree) / Bytes Utils
    - [center](#center)
    - [count](#count)
    - [decode](#decode)
    - [endswith](#endswith)
    - [find](#find)
    - [index](#index)
    - [removeprefix](#removeprefix)
    - [removesuffix](#removesuffix)
    - [replace](#replace)
    - [split](#split)
    - [startswith](#startswith)
    - [strip](#strip)

## center

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/bytes_utils.py#L7)

```python
@hof2
def center(length: SupportsIndex, fill_char: bytes, arg: bytes) -> bytes:
```

Point-free version of `bytes.center`.

#### Arguments

- `length` *SupportsIndex* - of result bytestring.
- `fill_char` *bytes* - to fill `bytes` around.
- `arg` *bytes* - to centralize.

#### See also

- [hof2](../core.md#hof2)

## count

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/bytes_utils.py#L19)

```python
@hof3
def count(sub: bytes, arg: bytes) -> int:
```

Point-free version of `bytes.count`.

#### Arguments

- `sub` *bytes* - substring to count.
- `arg` *bytes* - to count in.

#### Returns

- `int` - number of occurrences of `pattern` in `arg`.

#### See also

- [hof3](../core.md#hof3)

## decode

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/bytes_utils.py#L33)

```python
@hof1
@safe
def decode(encoding: str, arg: bytes) -> str:
```

Point-free version of `bytes.decode`.

#### Arguments

- `encoding` *str* - to decode with.
- `arg` *bytes* - to decode.

#### Returns

str | Exception: result.

#### See also

- [hof1](../core.md#hof1)
- [safe](../result.md#safe)

## endswith

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/bytes_utils.py#L48)

```python
@hof1
def endswith(sub: bytes, arg: bytes) -> bool:
```

Point-free version of `bytes.endswith`.

#### Arguments

- `sub` *bytes* - substring to check.
- `arg` *bytes* - to check in.

#### Returns

- `bool` - if `arg` endswith `sub`.

#### See also

- [hof1](../core.md#hof1)

## find

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/bytes_utils.py#L62)

```python
def find(sub: bytes, arg: bytes) -> int | None:
```

Point-free maybe version of `bytes.find`.

#### Arguments

- `sub` *bytes* - to search.
- `arg` *bytes* - to search int.

#### Returns

int | None: lowest index in arg where sub is found. `None` if nothing found.

## index

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/bytes_utils.py#L79)

```python
@hof1
@safe
def index(sub: bytes, arg: bytes) -> int:
```

Point-free version of `bytes.index`.

#### Arguments

- `sub` *bytes* - to search.
- `arg` *bytes* - to search in.

#### Returns

- `int` - lowest index in arg where `sub` is found. Raises error if nothing found.

#### See also

- [hof1](../core.md#hof1)
- [safe](../result.md#safe)

## removeprefix

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/bytes_utils.py#L94)

```python
@hof1
def removeprefix(prefix: bytes, arg: bytes) -> bytes:
```

Point-free version of `bytes.removeprefix`.

#### Arguments

- `prefix` *bytes* - to remove.
- `arg` *bytes* - to remove from.

#### Returns

- `bytes` - without prefix if it is possible.

#### See also

- [hof1](../core.md#hof1)

## removesuffix

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/bytes_utils.py#L108)

```python
@hof1
def removesuffix(suffix: bytes, arg: bytes) -> bytes:
```

Point-free version of `bytes.removesuffix`.

#### Arguments

- `suffix` *bytes* - to remove.
- `arg` *bytes* - to remove from.

#### Returns

- `bytes` - without suffix if it is possible.

#### See also

- [hof1](../core.md#hof1)

## replace

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/bytes_utils.py#L122)

```python
@hof2
def replace(old: bytes, new: bytes, arg: bytes) -> bytes:
```

Point-free version of `bytes.replace`.

#### Arguments

- `old` *bytes* - to replace.
- `new` *bytes* - to replace with.
- `arg` *bytes* - to replace in.

#### Returns

- `bytes` - result.

#### See also

- [hof2](../core.md#hof2)

## split

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/bytes_utils.py#L137)

```python
@hof1
def split(sep: bytes, arg: bytes) -> list[bytes]:
```

Point-free version of `bytes.split`.

#### Arguments

- `sep` *bytes* - to split with.
- `arg` *bytes* - to split.

#### Returns

- `list[bytes]` - result of split.

#### See also

- [hof1](../core.md#hof1)

## startswith

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/bytes_utils.py#L151)

```python
@hof1
def startswith(sub: bytes, arg: bytes) -> bool:
```

Point-free version of `bytes.startswith`.

#### Arguments

- `sub` *bytes* - substring to check.
- `arg` *bytes* - to check in.

#### Returns

- `bool` - if `arg` starts with `sub`.

#### See also

- [hof1](../core.md#hof1)

## strip

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/bytes_utils.py#L165)

```python
@hof1
def strip(chars: bytes, arg: bytes) -> bytes:
```

Point-free version of `bytes.strip`.

#### Arguments

- `chars` *bytes* - to strip.
- `arg` *bytes* - to strip from.

#### Returns

- `bytes` - result.

#### See also

- [hof1](../core.md#hof1)
