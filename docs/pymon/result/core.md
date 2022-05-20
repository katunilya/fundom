# Core

> Auto-generated documentation for [pymon.result.core](https://github.com/katunilya/pymon/blob/main/pymon/result/core.py) module.

- [Pymon](../../README.md#pymon-index) / [Modules](../../MODULES.md#pymon-modules) / [Pymon](../index.md#pymon) / [Result](index.md#result) / Core
    - [if_error](#if_error)
    - [if_error_returns](#if_error_returns)
    - [if_ok](#if_ok)
    - [safe](#safe)
    - [safe_async](#safe_async)

## if_error

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result/core.py#L25)

```python
def if_error(func: Callable[[TError], V]) -> Callable[[T | TError], T | V]:
```

Decorator that executes some function only on `Exception` input.

#### See also

- [TError](#terror)
- [V](#v)

## if_error_returns

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result/core.py#L39)

```python
@hof1
def if_error_returns(replacement: V, value: T | TError) -> V | T:
```

Replace `value` with `replacement` if one is `Exception`.

#### Arguments

- `replacement` *V* - to replace with.
value (T | TError): to replace.

#### Returns

V | T: error-safe result.

#### See also

- [V](#v)
- [hof1](../core.md#hof1)

## if_ok

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result/core.py#L11)

```python
def if_ok(func: Callable[[T], V]) -> Callable[[T | TError], V]:
```

Decorateor that protects function from being executed on `Exception` value.

#### See also

- [T](#t)
- [V](#v)

## safe

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result/core.py#L60)

```python
def safe(func: Callable[P, V]) -> Callable[P, V | TError]:
```

Decorator for sync function that might raise an exception.

Excepts exception and returns that instead.

#### See also

- [P](#p)
- [V](#v)

## safe_async

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result/core.py#L76)

```python
def safe_async(
    func: Callable[P, Awaitable[V]],
) -> Callable[P, Awaitable[V | TError]]:
```

Decorator for async function that might raise an exception.

Excepts exception and returns that instead.

#### See also

- [P](#p)
- [V](#v)
