# Dict Utils

> Auto-generated documentation for [pymon.pointfree.dict_utils](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/dict_utils.py) module.

- [Pymon](../../README.md#-pymon) / [Modules](../../MODULES.md#pymon-modules) / [Pymon](../index.md#pymon) / [Pointfree](index.md#pointfree) / Dict Utils
    - [maybe_get](#maybe_get)
    - [try_get](#try_get)

## maybe_get

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/dict_utils.py#L28)

```python
@hof1
def maybe_get(key: TKey, arg: dict[TKey, TValue]) -> TValue | None:
```

Point-free versuib if `dict.get` with default `None`.

#### Arguments

- `key` *TKey* - to get.
- `arg` *dict[TKey,TValue]* - to get from.

#### Returns

TValue | None: value.

#### See also

- [TKey](#tkey)
- [TValue](#tvalue)
- [hof1](../core.md#hof1)

## try_get

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/pointfree/dict_utils.py#L10)

```python
@hof1
@safe
def try_get(key: TKey, arg: dict[TKey, TValue]) -> TValue:
```

Point-free version of `dict[key]`.

Error-safe, returns `KeyError` in case key is not present and  `__missing__()` is
not provided.

#### Arguments

- `key` *TKey* - to get.
arg (dict[TKey, TValue]): to get from.

#### Returns

- `TValue` - value.

#### See also

- [TKey](#tkey)
- [TValue](#tvalue)
- [hof1](../core.md#hof1)
