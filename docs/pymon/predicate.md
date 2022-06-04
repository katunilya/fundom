# Predicate

> Auto-generated documentation for [pymon.predicate](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py) module.

- [Pymon](../README.md#-pymon) / [Modules](../MODULES.md#pymon-modules) / [Pymon](index.md#pymon) / Predicate
    - [FuturePredicate](#futurepredicate)
    - [Predicate](#predicate)
    - [future_predicate](#future_predicate)
    - [is_empty](#is_empty)
    - [is_not_empty](#is_not_empty)
    - [len_less_or_equals](#len_less_or_equals)
    - [len_less_then](#len_less_then)
    - [len_more_or_equals](#len_more_or_equals)
    - [len_more_then](#len_more_then)
    - [predicate](#predicate)

## FuturePredicate

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L11)

```python
class FuturePredicate(FutureFunc[P, bool]):
```

Abstraction over async predicates.

#### See also

- [P](#p)

## Predicate

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L60)

```python
dataclass(slots=True, frozen=True)
class Predicate(Func[P, bool]):
```

Abstraction over predicates.

#### See also

- [P](#p)

## future_predicate

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L107)

```python
def future_predicate(p: Callable[P, Awaitable[bool]]):
```

Makes function composable [FuturePredicate](#futurepredicate) instance.

#### See also

- [P](#p)

## is_empty

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L155)

```python
@predicate
def is_empty(obj: TSized) -> bool:
```

If `obj` is empty.

#### See also

- [TSized](#tsized)
- [predicate](#predicate)

## is_not_empty

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L161)

```python
@predicate
def is_not_empty(obj: TSized) -> bool:
```

If `obj` is not empty.

#### See also

- [TSized](#tsized)
- [predicate](#predicate)

## len_less_or_equals

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L132)

```python
def len_less_or_equals(length: int):
```

If `iterable` length is less or equals `length`.

## len_less_then

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L122)

```python
def len_less_then(length: int):
```

If `iterable` length is strictly less than `length`.

## len_more_or_equals

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L142)

```python
def len_more_or_equals(length: int):
```

If `iterable` length is more or equals `length`.

## len_more_then

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L112)

```python
def len_more_then(length: int):
```

If `iterable` length is strictly more than `length`.

## predicate

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/predicate.py#L102)

```python
def predicate(p: Callable[P, bool]):
```

Makes function composable [Predicate](#predicate) instance.

#### See also

- [P](#p)
