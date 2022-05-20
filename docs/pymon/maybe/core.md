# Core

> Auto-generated documentation for [pymon.maybe.core](https://github.com/katunilya/pymon/blob/main/pymon/maybe/core.py) module.

- [Pymon](../../README.md#pymon-index) / [Modules](../../MODULES.md#pymon-modules) / [Pymon](../index.md#pymon) / [Maybe](index.md#maybe) / Core
    - [if_none](#if_none)
    - [if_none_returns](#if_none_returns)
    - [if_some](#if_some)

## if_none

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/maybe/core.py#L24)

```python
def if_none(func: Callable[[None], V]) -> Callable[[T | None], V | None]:
```

Decorator that executes some function only on `None` input.

#### See also

- [V](#v)

## if_none_returns

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/maybe/core.py#L38)

```python
@hof1
def if_none_returns(replacement: V, value: T | None) -> V | T:
```

Replace `value` with `replacement` if one is `None`.

#### Arguments

- `replacement` *V* - to replace with.
value (T | None): to replace.

#### Returns

V | T: some result.

#### See also

- [V](#v)
- [hof1](../core.md#hof1)

## if_some

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/maybe/core.py#L10)

```python
def if_some(func: Callable[[T], V | None]) -> Callable[[T | None], V | None]:
```

Decorator that protects function from being executed on `None` value.

#### See also

- [T](#t)
