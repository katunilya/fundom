# Maybe

> Auto-generated documentation for [pymon.maybe](https://github.com/katunilya/pymon/blob/main/pymon/maybe.py) module.

- [Pymon](../README.md#-pymon) / [Modules](../MODULES.md#pymon-modules) / [Pymon](index.md#pymon) / Maybe
    - [choose_some](#choose_some)
    - [choose_some_future](#choose_some_future)
    - [if_none](#if_none)
    - [if_none_returns](#if_none_returns)
    - [if_some](#if_some)
    - [if_some_returns](#if_some_returns)
    - [some_when](#some_when)
    - [some_when_future](#some_when_future)

## choose_some

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/maybe.py#L159)

```python
dataclass(slots=True, init=False)
class choose_some(Generic[P, T]):
    def __init__() -> None:
```

Combines multiple sync functions into switch-case like statement.

The first function to return non-`None` result is used. If no function passed than
`None` is returned. Uses deepcopy to keep arguments immutable during attempts.

Examples

```python
f = (
    choose_some()
    | create_linked_node
    | create_isolated_node
)
```

#### See also

- [P](#p)
- [T](#t)

## choose_some_future

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/maybe.py#L196)

```python
dataclass(slots=True, init=False)
class choose_some_future(Generic[P, T]):
    def __init__() -> None:
```

Combines multiple sync functions into switch-case like statement.

The first function to return non-`None` result is used. If no function passed than
`None` is returned. Uses deepcopy to keep arguments immutable during attempts.

Examples

```python
f = (
    choose_some_future()
    | create_linked_node
    | create_isolated_node
)
```

#### See also

- [P](#p)
- [T](#t)

## if_none

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/maybe.py#L38)

```python
def if_none(func: Callable[[T], V]):
```

Decorator that executes some function only on `None` input.

Example

```python
result = (
    pipe({"body": b"hello", "status": 200})
    << (lambda dct: dct.get("Hello", None))
    << if_some(bytes_decode("UTF-8"))
    << if_none(lambda _: "")
)
```

#### See also

- [T](#t)
- [V](#v)

## if_none_returns

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/maybe.py#L62)

```python
@hof1
def if_none_returns(replacement: V, value: T) -> V | T:
```

Replace `value` with `replacement` if one is `None`.

#### Examples

```python
result = (
    pipe({"body": b"hello", "status": 200})
    << (lambda dct: dct.get("Hello", None))
    << if_some(bytes_decode("UTF-8"))
    << if_none_returns("")
)
```

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

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/maybe.py#L14)

```python
def if_some(func: Callable[[T], V]):
```

Decorator that protects function from being executed on `None` value.

Example

```python
result = (
    pipe({"body": b"hello", "status": 200})
    << (lambda dct: dct.get("Hello", None))
    << if_some(bytes_decode("UTF-8"))
    << if_none(lambda _: "")
)
```

#### See also

- [T](#t)
- [V](#v)

## if_some_returns

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/maybe.py#L89)

```python
@hof1
def if_some_returns(replacement: V, value: T) -> V | T:
```

Replace some `value` when it is not `None`.

#### Examples

```python
result = (
    pipe({"body": b"hello", "status": 200})
    << (lambda dct: dct.get("Hello", None))
    << if_some_returns(True)
    << if_none_returns(False)
)
```

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

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/maybe.py#L116)

```python
@hof1
def some_when(predicate: Callable[[T], bool], data: T) -> T | None:
```

Passes value next only when predicate is True, otherwise returns `None`.

#### Examples

```python
policy = some_when(lambda x: x > 3)
```

#### Arguments

predicate (Callable[[T], bool]): to fulfill.
- `data` *T* - to process.

#### Returns

T | None: result.

#### See also

- [T](#t)
- [hof1](core.md#hof1)

## some_when_future

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/maybe.py#L134)

```python
@hof1
@future.returns
async def some_when_future(
    predicate: Callable[[T], Awaitable[bool]],
    data: T,
) -> T | None:
```

Passes value next only when predicate is True, otherwise returns `None`.

#### Examples

```python
policy = some_when_future(more_than_3)
```

#### Arguments

predicate (Callable[[T], bool]): to fulfill.
- `data` *T* - to process.

#### Returns

T | None: result.

#### See also

- [T](#t)
- [hof1](core.md#hof1)
