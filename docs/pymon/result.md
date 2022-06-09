# Result

> Auto-generated documentation for [pymon.result](https://github.com/katunilya/pymon/blob/main/pymon/result.py) module.

- [Pymon](../README.md#-pymon) / [Modules](../MODULES.md#pymon-modules) / [Pymon](index.md#pymon) / Result
    - [PolicyViolationError](#policyviolationerror)
    - [check](#check)
    - [check_future](#check_future)
    - [choose_ok](#choose_ok)
    - [choose_ok_future](#choose_ok_future)
    - [if_error](#if_error)
    - [if_error_returns](#if_error_returns)
    - [if_ok](#if_ok)
    - [ok_when](#ok_when)
    - [ok_when_future](#ok_when_future)
    - [safe](#safe)
    - [safe_future](#safe_future)

## PolicyViolationError

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L137)

```python
dataclass(slots=True, frozen=True)
class PolicyViolationError(Exception):
```

Exception that marks that policy is violated.

## check

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L143)

```python
def check(predicate: Callable[P, bool]) -> T | PolicyViolationError:
```

Pass value next only if predicate is True, otherwise policy is violated.

#### Arguments

- `predicate` *Predicate[T]* - to check.

#### Returns

T | PolicyViolationError: result

#### See also

- [P](#p)

## check_future

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L155)

```python
def check_future(
    predicate: Callable[P, Awaitable[bool]],
) -> future[T] | future[PolicyViolationError]:
```

Pass value next only if predicate is True, otherwise policy is violated.

#### Arguments

predicate (Callable[P, Future[bool]]): to check.

#### Returns

Future[T] | Future[PolicyViolationError]: result.

#### See also

- [P](#p)

## choose_ok

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L169)

```python
def choose_ok(*funcs: Callable[[T], V | TError]) -> Callable[[T], V | TError]:
```

Combines multiple sync functions that might return error into one.

Result of the first function to return non-Exception result is returned.

#### See also

- [T](#t)

## choose_ok_future

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L190)

```python
def choose_ok_future(
    *funcs: Callable[[T], future[V | TError]],
) -> Callable[[T], future[V | TError]]:
```

Combines multiple async functions that might return error into one.

Result of the first function to return non-Exception result is returned.

#### See also

- [T](#t)

## if_error

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L26)

```python
def if_error(func: Callable[[T], V]):
```

Decorator that executes some function only on `Exception` input.

#### See also

- [T](#t)
- [V](#v)

## if_error_returns

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L40)

```python
@hof1
def if_error_returns(replacement: V, value: T) -> V | T:
```

Replace `value` with `replacement` if one is `Exception`.

#### Arguments

- `replacement` *V* - to replace with.
value (T | TError): to replace.

#### Returns

V | T: error-safe result.

#### See also

- [T](#t)
- [V](#v)
- [hof1](core.md#hof1)

## if_ok

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L12)

```python
def if_ok(func: Callable[[T], V]):
```

Decorator that protects function from being executed on `Exception` value.

#### See also

- [T](#t)
- [V](#v)

## ok_when

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L94)

```python
@hof2
def ok_when(
    predicate: Callable[[T], bool],
    error: TError,
    value: T,
) -> T | TError:
```

Pass value only if predicate is True, otherwise return error.

#### Arguments

predicate (Callable[[T], bool]): to fulfill.
- `error` *TError* - to replace with.
- `value` *T* - to process.

#### Returns

T | TError: result.

#### See also

- [TError](#terror)
- [T](#t)
- [hof2](core.md#hof2)

## ok_when_future

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L119)

```python
@hof2
def ok_when_future(
    predicate: Callable[[T], Awaitable[bool]],
    error: TError,
    value: T,
) -> future[T] | future[TError]:
```

Pass value only if async predicate is True, otherwise return error.

#### Arguments

predicate (Callable[[T], bool]): to fulfill.
- `error` *TError* - to replace with.
- `value` *T* - to process.

#### Returns

Future[T] | Future[TError]: result.

#### See also

- [TError](#terror)
- [T](#t)
- [hof2](core.md#hof2)

## safe

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L61)

```python
def safe(func: Callable[P, V]) -> Callable[P, V | Exception]:
```

Decorator for sync function that might raise an exception.

Excepts exception and returns that instead.

#### See also

- [P](#p)
- [V](#v)

## safe_future

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L77)

```python
def safe_future(
    func: Callable[P, Awaitable[V]],
) -> Callable[P, future[V | TError]]:
```

Decorator for async function that might raise an exception.

Excepts exception and returns that instead.

#### See also

- [P](#p)
- [V](#v)
