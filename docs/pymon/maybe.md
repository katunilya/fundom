# Maybe

> Auto-generated documentation for [pymon.maybe](https://github.com/katunilya/pymon/blob/main/pymon/maybe.py) module.

- [Pymon](../README.md#-pymon) / [Modules](../MODULES.md#pymon-modules) / [Pymon](index.md#pymon) / Maybe
    - [if_none](#if_none)
    - [if_none_returns](#if_none_returns)
    - [if_some](#if_some)
    - [if_some_returns](#if_some_returns)
    - [some_when](#some_when)

## if_none

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/maybe.py#L24)

```python
def if_none(func: Callable[[T], V]):
```

Decorator that executes some function only on `None` input.

#### See also

- [T](#t)
- [V](#v)

## if_none_returns

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/maybe.py#L38)

```python
@hof1
def if_none_returns(replacement: V, value: T) -> V | T:
```

Replace `value` with `replacement` if one is `None`.

#### Arguments

- `replacement` *V* - to replace with.
- `value` *T* - to replace.

#### Returns

V | T: some result.

#### See also

- [T](#t)
- [V](#v)
- [hof1](core.md#hof1)

## if_some

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/maybe.py#L10)

```python
def if_some(func: Callable[[T], V]):
```

Decorator that protects function from being executed on `None` value.

#### See also

- [T](#t)
- [V](#v)

## if_some_returns

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/maybe.py#L56)

```python
@hof1
def if_some_returns(replacement: V, value: T) -> V | T:
```

Replace some `value` when it is not `None`.

#### Arguments

- `replacement` *V* - to replace with.
- `value` *T* - to replace.

#### Returns

V | T: some result.

#### See also

- [T](#t)
- [V](#v)
- [hof1](core.md#hof1)

## some_when

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/maybe.py#L74)

```python
@hof1
def some_when(predicate: Callable[[T], bool], data: T) -> T | None:
```

Passes value next only when predicate is True, otherwise returns `None`.

#### Arguments

predicate (Callable[[T], bool]): to fulfill.
- `data` *T* - to process.

#### Returns

T | None: result.

#### See also

- [T](#t)
- [hof1](core.md#hof1)
