# Predicate

> Auto-generated documentation for [pymon.predicate](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py) module.

- [Pymon](../README.md#-pymon) / [Modules](../MODULES.md#pymon-modules) / [Pymon](index.md#pymon) / Predicate
    - [Predicate](#predicate)
    - [is_empty](#is_empty)
    - [is_not_empty](#is_not_empty)
    - [len_less_or_equals](#len_less_or_equals)
    - [len_less_then](#len_less_then)
    - [len_more_or_equals](#len_more_or_equals)
    - [len_more_then](#len_more_then)
    - [predicate](#predicate)

## Predicate

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L8)

```python
dataclass(frozen=True, slots=True)
class Predicate(Callable[[T], bool]):
```

Abstraction over predicates for seamless composition of predicate functions.

#### See also

- [T](#t)

## is_empty

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L63)

```python
@predicate
def is_empty(obj: TSized) -> bool:
```

If `obj` is empty.

#### See also

- [TSized](#tsized)
- [predicate](#predicate)

## is_not_empty

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L69)

```python
@predicate
def is_not_empty(obj: TSized) -> bool:
```

If `obj` is not empty.

#### See also

- [TSized](#tsized)
- [predicate](#predicate)

## len_less_or_equals

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L50)

```python
def len_less_or_equals(length: int) -> Predicate[Iterable]:
```

If `iterable` length is less or equals `length`.

## len_less_then

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L45)

```python
def len_less_then(length: int) -> Predicate[Iterable]:
```

If `iterable` length is strictly less than `length`.

## len_more_or_equals

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L55)

```python
def len_more_or_equals(length: int) -> Predicate[Iterable]:
```

If `iterable` length is more or equals `length`.

## len_more_then

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L40)

```python
def len_more_then(length: int) -> Predicate[Iterable]:
```

If `iterable` length is strictly more than `length`.

## predicate

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L35)

```python
def predicate(func: Callable[[T], bool]) -> Predicate[T]:
```

Makes function composable [Predicate](#predicate) instance.

#### See also

- [T](#t)
