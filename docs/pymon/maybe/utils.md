# Utils

> Auto-generated documentation for [pymon.maybe.utils](https://github.com/katunilya/pymon/blob/main/pymon/maybe/utils.py) module.

- [Pymon](../../README.md#pymon-index) / [Modules](../../MODULES.md#pymon-modules) / [Pymon](../index.md#pymon) / [Maybe](index.md#maybe) / Utils
    - [maybe_get](#maybe_get)
    - [some_when](#some_when)

## maybe_get

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/maybe/utils.py#L9)

```python
@hof1
def maybe_get(key: TKey, dct: dict[TKey, TValue]) -> TValue | None:
```

Maybe get some value from dictionary.

#### Arguments

- `key` *TKey* - of dict.
dct (dict[TKey, TValue]): dictionary.

#### Returns

TValue | None: value of key if one is present.

#### See also

- [TKey](#tkey)
- [TValue](#tvalue)
- [hof1](../core.md#hof1)

## some_when

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/maybe/utils.py#L26)

```python
@hof1
def some_when(predicate: Callable[[T], bool], data: T) -> T | None:
```

Passes value next only when predicate is True, otherwise returns `None`.

#### Arguments

predicate (Callable[[T], bool]): to fulfill.
- `data` *T* - to process.

#### Returns

T | None: retult.

#### See also

- [T](#t)
- [hof1](../core.md#hof1)
