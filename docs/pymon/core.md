# Core

> Auto-generated documentation for [pymon.core](https://github.com/katunilya/pymon/blob/main/pymon/core.py) module.

- [Pymon](../README.md#-pymon) / [Modules](../MODULES.md#pymon-modules) / [Pymon](index.md#pymon) / Core
    - [compose](#compose)
    - [future](#future)
        - [future.returns](#futurereturns)
    - [pipe](#pipe)
        - [pipe().finish](#pipefinish)
        - [pipe.returns](#pipereturns)
    - [cfilter](#cfilter)
    - [cmap](#cmap)
    - [foldl](#foldl)
    - [foldr](#foldr)
    - [hof1](#hof1)
    - [hof2](#hof2)
    - [hof3](#hof3)
    - [returns](#returns)
    - [returns_future](#returns_future)
    - [this](#this)
    - [this_future](#this_future)

## compose

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L268)

```python
dataclass(slots=True, init=False)
class compose(Generic[P, V]):
    def __init__() -> None:
```

Function composition abstraction.

If no function is passed to composition than `Exception` would be raised on call.

Example

```python
f: Callable[[int], int] = (
    compose()
    << (lambda x: x + 1)
    << (lambda x: x ** 2)
)
```

#### See also

- [P](#p)
- [V](#v)

## future

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L25)

```python
dataclass(slots=True, frozen=True)
class future(Generic[T]):
```

Abstraction over awaitable value to run in pipeline.

Example

```python
result = await (
    future(get_user_async)
    << if_role_is("moderator")
    << set_role("admin")
    >> update_user_async
)
```

#### See also

- [T](#t)

### future.returns

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L55)

```python
@staticmethod
def returns(func: Callable[P, Coroutine[Any, Any, T]]):
```

Wraps returned value of async function to [future](#future).

Return value of function is wrapped into [future](#future).

Example

```python
@future.returns
async def some_async_func(x: int, y: int) -> str:
    ...
```

#### See also

- [P](#p)
- [T](#t)

## pipe

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L80)

```python
dataclass(slots=True, frozen=True)
class pipe(Generic[T]):
```

Abstraction over some value to run in pipeline.

Example

```python
result: int = (
    pipe(12)
    << (lambda x: x + 1)
    << (lambda x: x**2)
    << (lambda x: x // 3)
).finish()
```

#### See also

- [T](#t)

### pipe().finish

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L101)

```python
def finish() -> T:
```

Finish [pipe](#pipe) by unpacking internal value.

#### Examples

```python
result = (
    pipe(3)
    << (lambda x: x + 1)
    << (lambda x: x**2)
)
value = result.finish()
```

#### Returns

- `T` - internal value

#### See also

- [T](#t)

### pipe.returns

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L118)

```python
@staticmethod
def returns(func: Callable[P, pipe[T]]) -> Callable[P, T]:
```

Decorator for functions that return [pipe](#pipe) object for seamless unwrapping.

Example

```python
@pipe.returns
def some_function(x: int) -> pipe[bool]:
    return (
        pipe(x)
        << (lambda x: x + 1)
        << some_when(lambda x: x > 10)
        << if_some_returns(True)
        << if_none_returns(False)

# returned type is bool
```

#### See also

- [P](#p)
- [T](#t)

## cfilter

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L401)

```python
@hof1
def cfilter(
    predicate: Callable[[A1], bool],
    lst: Iterable[A1],
) -> Iterable[A1]:
```

Curried `filter` function.

#### Arguments

predicate (Callable[[A1], bool]): to filter with.
- `lst` *Iterable[A1]* - to filter.

#### Returns

- `Iterable[A1]` - filtered iterable.

#### See also

- [A1](#a1)
- [hof1](#hof1)

## cmap

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L387)

```python
@hof1
def cmap(mapper: Callable[[A1], A2], lst: Iterable[A1]) -> Iterable[A2]:
```

Curried `map` function.

#### Arguments

mapper (Callable[[A1], A2]): mapper for element of iterable.
- `lst` *Iterable[A1]* - to map.

#### Returns

- `Iterable[A2]` - map result.

#### See also

- [A1](#a1)
- [A2](#a2)
- [hof1](#hof1)

## foldl

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L357)

```python
@hof2
def foldl(
    folder: Callable[[A1, A2], A1],
    initial: A1,
    lst: Iterable[A2],
) -> A1:
```

Curried `reduce` left function.

#### Arguments

folder (Callable[[A1, A2], A1]): aggregator.
- `initial` *A1* - initial aggregation value.
- `lst` *Iterable[A2]* - data to reduce.

#### Returns

- `A1` - reduction result.

#### See also

- [A1](#a1)
- [A2](#a2)
- [hof2](#hof2)

## foldr

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L372)

```python
@hof2
def foldr(
    folder: Callable[[A1, A2], A2],
    initial: A2,
    lst: Iterable[A1],
) -> A2:
```

Curried `reduce` right function.

#### Arguments

folder (Callable[[A1, A2], A2]): aggregator.
- `initial` *A2* - initial aggregation value.
- `lst` *Iterable[A1]* - data to reduce.

#### Returns

- `A2` - reduction result.

#### See also

- [A1](#a1)
- [A2](#a2)
- [hof2](#hof2)

## hof1

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L318)

```python
def hof1(f: Callable[Concatenate[A1, P], AResult]):
```

Separate first argument from other.

#### See also

- [A1](#a1)
- [AResult](#aresult)
- [P](#p)

## hof2

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L331)

```python
def hof2(f: Callable[Concatenate[A1, A2, P], AResult]):
```

Separate first 2 arguments from other.

#### See also

- [A1](#a1)
- [A2](#a2)
- [AResult](#aresult)
- [P](#p)

## hof3

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L344)

```python
def hof3(f: Callable[Concatenate[A1, A2, A3, P], AResult]):
```

Separate first 3 arguments from other.

#### See also

- [A1](#a1)
- [A2](#a2)
- [A3](#a3)
- [AResult](#aresult)
- [P](#p)

## returns

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L167)

```python
def returns(x: T) -> Callable[P, T]:
```

Return `T` on any input.

Example

```python
get_none: Callable[..., None] = returns(None)
```

#### See also

- [P](#p)
- [T](#t)

## returns_future

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L181)

```python
def returns_future(x: T) -> Callable[P, future[T]]:
```

Return awaitable `T` on any input.

Example

```python
get_none_future: Callable[..., future[None]] = returns_future(None)
```

#### See also

- [P](#p)
- [T](#t)

## this

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L146)

```python
def this(args: T) -> T:
```

Synchronous identity function.

Example

```python
this(3)  # 3
```

#### See also

- [T](#t)

## this_future

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L156)

```python
@future.returns
async def this_future(args: T) -> T:
```

Asynchronous identity function.

Example

```python
this_future(3)  # future(3)
```

#### See also

- [T](#t)
