# Str Utils

> Auto-generated documentation for [pymon.pointfree.str_utils](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/str_utils.py) module.

- [Pymon](../../README.md#-pymon) / [Modules](../../MODULES.md#pymon-modules) / [Pymon](../index.md#pymon) / [Pointfree](index.md#pointfree) / Str Utils
    - [center](#center)
    - [count](#count)
    - [encode](#encode)
    - [endswith](#endswith)
    - [find](#find)
    - [index](#index)
    - [join](#join)
    - [join_by](#join_by)
    - [removeprefix](#removeprefix)
    - [removesuffix](#removesuffix)
    - [replace](#replace)
    - [split](#split)
    - [startswith](#startswith)
    - [strip](#strip)

## center

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/str_utils.py#L7)

```python
@hof2
def center(length: SupportsIndex, fillchar: str, arg: str) -> str:
```

Point-free version of `str.center`.

#### Arguments

- `length` *SupportsIndex* - of result string.
- `fillchar` *str* - to fill `str` around.
- `arg` *str* - to centralize.

#### See also

- [hof2](../core.md#hof2)

## count

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/str_utils.py#L19)

```python
@hof3
def count(sub: str, arg: str) -> int:
```

Point-free version of `str.count`.

#### Arguments

- `sub` *str* - substring to count.
- `arg` *str* - to count in.

#### Returns

- `int` - number of occurances of `pattern` in `arg`.

#### See also

- [hof3](../core.md#hof3)

## encode

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/str_utils.py#L33)

```python
@hof1
@safe
def encode(encoding: str, arg: str) -> bytes:
```

Point-free version of `str.encode`.

#### Arguments

- `encoding` *str* - to encode with.
- `arg` *str* - to encode.

#### Returns

bytes | Exception: result

#### See also

- [hof1](../core.md#hof1)
- [safe](../result.md#safe)

## endswith

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/str_utils.py#L48)

```python
@hof1
def endswith(sub: str, arg: str) -> bool:
```

Point-free version of `str.endswith`.

#### Arguments

- `sub` *str* - substring to check.
- `arg` *str* - to check in.

#### Returns

- `bool` - if `arg` endswith `sub`.

#### See also

- [hof1](../core.md#hof1)

## find

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/str_utils.py#L62)

```python
def find(sub: str, arg: str) -> int | None:
```

Point-free maybe version of `str.find`.

#### Arguments

- `sub` *str* - to serach.
- `arg` *str* - to search int.

#### Returns

int | None: lowest index in arg where sub is found. `None` if nothing found.

## index

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/str_utils.py#L79)

```python
@hof1
@safe
def index(sub: str, arg: str) -> int:
```

Point-free version of `str.index`.

#### Arguments

- `sub` *str* - to search.
- `arg` *str* - to search in.

#### Returns

- `int` - lowest index in arg where `sub` is found. Raises error if nothing found.

#### See also

- [hof1](../core.md#hof1)
- [safe](../result.md#safe)

## join

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/str_utils.py#L108)

```python
@hof1
def join(iterable: Iterable[str], arg: str) -> str:
```

Point-free version of `str.join`.

#### Arguments

- `iterable` *Iterable[str]* - to join.
- `arg` *str* - to join with.

#### Returns

- `str` - joined string.

#### See also

- [hof1](../core.md#hof1)

## join_by

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/str_utils.py#L94)

```python
@hof1
def join_by(concatenator: str, arg: Iterable[str]) -> str:
```

Join incoming `Iterable[str]` by some `concatenatror`.

#### Arguments

- `concatenator` *str* - to join with.
- `arg` *Iterable[str]* - to be joined.

#### Returns

- `str` - joined string.

#### See also

- [hof1](../core.md#hof1)

## removeprefix

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/str_utils.py#L122)

```python
@hof1
def removeprefix(prefix: str, arg: str) -> str:
```

Point-free version of `str.removeprefix`.

#### Arguments

- `prefix` *str* - to remove.
- `arg` *str* - to remove from.

#### Returns

- `str` - if the string starts with the prefix string, return string[len(prefix):].
Otherwise, return a copy of the original string:

#### See also

- [hof1](../core.md#hof1)

## removesuffix

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/str_utils.py#L137)

```python
@hof1
def removesuffix(suffix: str, arg: str) -> str:
```

Point-free version of `str.removesuffix`.

#### Arguments

- `suffix` *str* - to remove.
- `arg` *str* - to remove from.

#### Returns

- `str` - If the string ends with the suffix string and that suffix is not empty,
return string[:-len(suffix)]. Otherwise, return a copy of the original string:

#### See also

- [hof1](../core.md#hof1)

## replace

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/str_utils.py#L152)

```python
@hof2
def replace(old: str, new: str, arg: str) -> str:
```

Point-free version of `str.replace`.

#### Arguments

- `old` *str* - to replace.
- `new` *str* - to replace with.
- `arg` *str* - to replace in.

#### Returns

- `str` - result.

#### See also

- [hof2](../core.md#hof2)

## split

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/str_utils.py#L167)

```python
@hof1
def split(sep: str, arg: str) -> list[str]:
```

Point-free version of `str.split`.

#### Arguments

- `sep` *str* - to split with.
- `arg` *str* - to split.

#### Returns

- `list[str]` - result of split.

#### See also

- [hof1](../core.md#hof1)

## startswith

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/str_utils.py#L181)

```python
@hof1
def startswith(sub: str, arg: str) -> bool:
```

Point-free version of `str.startswith`.

#### Arguments

- `sub` *str* - substring to check.
- `arg` *str* - to check in.

#### Returns

- `bool` - if `arg` starts with `sub`.

#### See also

- [hof1](../core.md#hof1)

## strip

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/str_utils.py#L195)

```python
@hof1
def strip(chars: str, arg: str) -> str:
```

Point-free version of `str.strip`.

#### Arguments

- `chars` *str* - to strip.
- `arg` *str* - to strip from.

#### Returns

- `str` - result.

#### See also

- [hof1](../core.md#hof1)
