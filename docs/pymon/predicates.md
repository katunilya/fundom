# Predicates

> Auto-generated documentation for [pymon.predicates](https://github.com/katunilya/pymon/blob/main/pymon/predicates.py) module.

- [Pymon](../README.md#-pymon) / [Modules](../MODULES.md#pymon-modules) / [Pymon](index.md#pymon) / Predicates
    - [is_empty](#is_empty)
    - [is_not_empty](#is_not_empty)
    - [len_less_or_equals](#len_less_or_equals)
    - [len_less_then](#len_less_then)
    - [len_more_or_equals](#len_more_or_equals)
    - [len_more_then](#len_more_then)

## is_empty

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicates.py#L33)

```python
def is_empty(obj: TSized) -> bool:
```

If `obj` is empty.

#### See also

- [TSized](#tsized)

## is_not_empty

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicates.py#L38)

```python
def is_not_empty(obj: TSized) -> bool:
```

If `obj` is not empty.

#### See also

- [TSized](#tsized)

## len_less_or_equals

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicates.py#L18)

```python
@hof1
def len_less_or_equals(length: int, iterable: Iterable) -> bool:
```

If `iterable` length is less or equals `length`.

#### See also

- [hof1](core.md#hof1)

## len_less_then

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicates.py#L12)

```python
@hof1
def len_less_then(length: int, iterable: Iterable) -> bool:
```

If `iterable` length is strictly less than `length`.

#### See also

- [hof1](core.md#hof1)

## len_more_or_equals

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicates.py#L24)

```python
@hof1
def len_more_or_equals(length: int, iterable: Iterable) -> bool:
```

If `iterable` length is more or equals `length`.

#### See also

- [hof1](core.md#hof1)

## len_more_then

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicates.py#L6)

```python
@hof1
def len_more_then(length: int, iterable: Iterable) -> bool:
```

If `iterable` length is strictly more than `length`.

#### See also

- [hof1](core.md#hof1)
