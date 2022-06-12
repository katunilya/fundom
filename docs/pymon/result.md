# Result

> Auto-generated documentation for [pymon.result](https://github.com/katunilya/pymon/blob/main/pymon/result.py) module.

- [Pymon](../README.md#-pymon) / [Modules](../MODULES.md#pymon-modules) / [Pymon](index.md#pymon) / Result
    - [EmptyChooseOkError](#emptychooseokerror)
    - [FailedChooseOkError](#failedchooseokerror)
    - [choose_ok](#choose_ok)
    - [choose_ok_future](#choose_ok_future)
    - [if_error](#if_error)
    - [if_error_returns](#if_error_returns)
    - [if_ok](#if_ok)
    - [if_ok_returns](#if_ok_returns)
    - [ok_when](#ok_when)
    - [ok_when_future](#ok_when_future)
    - [safe](#safe)
    - [safe_future](#safe_future)

## EmptyChooseOkError

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L221)

```python
class EmptyChooseOkError(Exception):
```

Returned when [choose_ok](#choose_ok) or [choose_ok_future](#choose_ok_future) has no options.

## FailedChooseOkError

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L225)

```python
class FailedChooseOkError(Exception, Generic[P]):
    def __init__(*args: P.args, **_: P.kwargs) -> None:
```

Returned when no function in [choose_ok](#choose_ok) or [choose_ok_future](#choose_ok_future) succeeded.

#### See also

- [P](#p)

## choose_ok

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L233)

```python
dataclass(slots=True, init=False)
class choose_ok(Generic[P, T]):
    def __init__() -> None:
```

Combines multiple sync functions into switch-case like statement.

The first function to return non-`Exception` result is used. If no function passed
than [EmptyChooseOkError](#emptychooseokerror) is raised. Uses deepcopy to keep arguments immutable
during attempts.

Examples

```python
f = (
    choose_ok()
    | create_linked_node
    | create_isolated_node
)
```

#### See also

- [P](#p)
- [T](#t)

## choose_ok_future

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L274)

```python
dataclass(slots=True, init=False)
class choose_ok_future(Generic[P, T]):
    def __init__() -> None:
```

Combines multiple async functions into switch-case like statement.

The first function to return non-`Exception` result is used. If no function passed
than [EmptyChooseOkError](#emptychooseokerror) is raised. Uses deepcopy to keep arguments immutable
during attempts.

Examples

```python
f = (
    choose_ok_future()
    | create_linked_node
    | create_isolated_node
)
```

#### See also

- [P](#p)
- [T](#t)

## if_error

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L39)

```python
def if_error(func: Callable[[T], V]):
```

Decorator that executes some function only on `Exception` input.

Example

```python
result = (
    pipe({"body": b"hello", "status": 200})
    << safe(lambda dct: dct["Hello"])
    << if_ok(bytes_decode("UTF-8"))
    << if_error(lambda err: str(err))
)
```

#### See also

- [T](#t)
- [V](#v)

## if_error_returns

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L91)

```python
@hof1
def if_error_returns(replacement: V, value: T) -> V | T:
```

Replace `value` with `replacement` if one is `Exception`.

#### Examples

```python
result = (
    pipe({"body": "hello", "status": 200})
    << get("body")
    << if_error_returns("")
)
```

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

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L15)

```python
def if_ok(func: Callable[[T], V]):
```

Decorator that protects function from being executed on `Exception` value.

Example

```python
result = (
    pipe({"body": b"hello", "status": 200})
    << safe(lambda dct: dct["Hello"])
    << if_ok(bytes_decode("UTF-8"))
    << if_error(lambda err: str(err))
)
```

#### See also

- [T](#t)
- [V](#v)

## if_ok_returns

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L63)

```python
@hof1
def if_ok_returns(replacement: V, value: T) -> V | T:
```

Replace `value` with `replacement` if one is not `Exception`.

#### Examples

```python
result = (
    pipe({"body": b"hello", "status": 200})
    << get("body")
    << if_ok_returns("Ok")
    << if_error_returns("")
)
```

#### Arguments

- `replacement` *V* - to replace with.
- `value` *T* - to replace.

#### Returns

V | T: error-safe result.

#### See also

- [T](#t)
- [V](#v)
- [hof1](core.md#hof1)

## ok_when

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L169)

```python
@hof2
def ok_when(
    predicate: Callable[[T], bool],
    create_error: Callable[[T], TError],
    value: T,
) -> T | TError:
```

Pass value only if predicate is True, otherwise return error.

#### Examples

```python
policy = ok_when(lambda x: x > 10, lambda _: Exception("More than 10"))
```

#### Arguments

predicate (Callable[[T], bool]): to fulfill.
create_error (Callable[[T], TError]): factory function for error.
- `value` *T* - to process.

#### Returns

T | TError: result.

#### See also

- [TError](#terror)
- [T](#t)
- [hof2](core.md#hof2)

## ok_when_future

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L198)

```python
@hof2
def ok_when_future(
    predicate: Callable[[T], Awaitable[bool]],
    create_error: Callable[[T], TError],
    value: T,
) -> future[T] | future[TError]:
```

Pass value only if async predicate is True, otherwise return error.

#### Examples

```python
policy = ok_when_future(more_than_10, lambda _: Exception("More than 10"))
```

#### Arguments

predicate (Callable[[T], bool]): to fulfill.
create_error (Callable[[T], TError]): factory function for error.
- `value` *T* - to process.

#### Returns

future[T] | future[TError]: result.

#### See also

- [TError](#terror)
- [T](#t)
- [hof2](core.md#hof2)

## safe

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L120)

```python
def safe(func: Callable[P, V]) -> Callable[P, V | Exception]:
```

Decorator for sync function that might raise an exception.

Excepts exception and returns that instead.

Example

```python
@safe
def get_key(key: Any, dct: dict) -> Any:
    return dct[key]  # raises error

# type: str, dict -> Any | Exception
```

#### See also

- [P](#p)
- [V](#v)

## safe_future

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/result.py#L144)

```python
def safe_future(
    func: Callable[P, Awaitable[V]],
) -> Callable[P, future[V | TError]]:
```

Decorator for async function that might raise an exception.

Excepts exception and returns that instead.

Example

```python
@safe_future
async def connect_database(conn_str: str) -> Database:
    return Database(conn_str)

# type: str -> Database | Exception
```

#### See also

- [P](#p)
- [V](#v)
