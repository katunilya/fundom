# Predicate

> Auto-generated documentation for [pymon.predicate](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py) module.

- [Pymon](../README.md#-pymon) / [Modules](../MODULES.md#pymon-modules) / [Pymon](index.md#pymon) / Predicate
    - [each](#each)
    - [one](#one)
    - [is_empty](#is_empty)
    - [is_not_empty](#is_not_empty)
    - [len_less_or_equals](#len_less_or_equals)
    - [len_less_then](#len_less_then)
    - [len_more_or_equals](#len_more_or_equals)
    - [len_more_then](#len_more_then)

## each

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L44)

```python
dataclass(slots=True, init=False)
class each(Generic[P]):
    def __init__() -> None:
```

Mathematical conjunction of predicates.

If no predicate passed returns True.

Example

```python
# returns True if number is between 3 and 10
p: Callable[[int], bool] = (
    each()
    << (lambda x: x > 3)
    << (lambda x: x < 10)
)
```

#### See also

- [P](#p)

## one

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L114)

```python
dataclass(slots=True, init=False)
class one(Generic[P]):
    def __init__() -> None:
```

Mathematical disjunction of predicates.

If no predicate passed returns False.

Example

```python
# returns True for any number that is less than 3 or more than 10
p: Callable[[int], bool] = (
    one()
    << (lambda x < 3)
    << (lambda x > 10)
)
```

#### See also

- [P](#p)

## is_empty

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L189)

```python
def is_empty(obj: TSized) -> bool:
```

If `obj` is empty.

#### See also

- [TSized](#tsized)

## is_not_empty

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L194)

```python
def is_not_empty(obj: TSized) -> bool:
```

If `obj` is not empty.

#### See also

- [TSized](#tsized)

## len_less_or_equals

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L168)

```python
def len_less_or_equals(length: int):
```

If `iterable` length is less or equals `length`.

## len_less_then

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L159)

```python
def len_less_then(length: int):
```

If `iterable` length is strictly less than `length`.

## len_more_or_equals

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L177)

```python
def len_more_or_equals(length: int):
```

If `iterable` length is more or equals `length`.

## len_more_then

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L150)

```python
def len_more_then(length: int):
```

If `iterable` length is strictly more than `length`.
