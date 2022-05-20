# Core

> Auto-generated documentation for [pymon.core](https://github.com/katunilya/pymon/blob/main/pymon/core.py) module.

- [Pymon](../README.md#-pymon) / [Modules](../MODULES.md#pymon-modules) / [Pymon](index.md#pymon) / Core
    - [Future](#future)
        - [Future().then](#futurethen)
        - [Future().then_async](#futurethen_async)
    - [Pipe](#pipe)
        - [Pipe().finish](#pipefinish)
        - [Pipe().then](#pipethen)
        - [Pipe().then_async](#pipethen_async)
    - [cfilter](#cfilter)
    - [cmap](#cmap)
    - [creducel](#creducel)
    - [creducer](#creducer)
    - [hof1](#hof1)
    - [hof2](#hof2)
    - [hof3](#hof3)
    - [pipeline](#pipeline)
    - [returns](#returns)
    - [returns_async](#returns_async)
    - [returns_future](#returns_future)
    - [this](#this)
    - [this_async](#this_async)

## Future

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L23)

```python
dataclass(slots=True, frozen=True)
class Future(Generic[T]):
```

Abstraction over awaitable value to run in pipeline.

Example

```python
result = await (
    Future(get_user_async)
    << if_role_is("moderator")
    << set_role("admin")
    >> update_user_async
)
```

#### See also

- [T](#t)

### Future().then

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L43)

```python
def then(func: Callable[[T], V]) -> Future[V]:
```

Execute sync `func` next on awaited internal value.

#### Arguments

func (Callable[[T], V]): to execute.

#### Returns

- `Future[V]` - awaitable result of execution.

#### See also

- [T](#t)
- [V](#v)

### Future().then_async

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L57)

```python
def then_async(func: Callable[[T], Awaitable[V]]) -> Future[V]:
```

Execute async `func` next on awaited internal value.

#### Arguments

func (Callable[[T], Awaitable[V]]): to execute.

#### Returns

- `Future[V]` - awaitable result of execution.

#### See also

- [T](#t)
- [V](#v)

## Pipe

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L90)

```python
dataclass(slots=True, frozen=True)
class Pipe(Generic[T]):
```

Abstraction over some value to run in pipeline.

Example

```python
result: int = (
    Pipe(12)
    << (lambda x: x + 1)
    << (lambda x: x**2)
    << (lambda x: x // 3)
).finish()
```

#### See also

- [T](#t)

### Pipe().finish

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L134)

```python
def finish() -> T:
```

Finish [Pipe](#pipe) by unpacking internal value.

#### Returns

- `T` - internal value

#### See also

- [T](#t)

### Pipe().then

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L104)

```python
def then(func: Callable[[T], V]) -> Pipe[V]:
```

Execute sync `func` next on internal value.

#### Arguments

func (Callable[[T], V]): to execute.

#### Returns

- `Pipe[V]` - execution result.

#### See also

- [T](#t)
- [V](#v)

### Pipe().then_async

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L115)

```python
def then_async(func: Callable[[T], Awaitable[V]]) -> Future[V]:
```

Execute async `func` next on internal value.

Returns [Future](#future) for further pipeline.

#### Arguments

func (Callable[[T], Awaitable[V]]): to execute.

#### Returns

- `Future[V]` - execution result.

#### See also

- [T](#t)
- [V](#v)

## cfilter

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L272)

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

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L258)

```python
@hof1
def cmap(mapper: Callable[[A1], A2], lst: Iterable[A1]) -> Iterable[A2]:
```

Curreid `map` function.

#### Arguments

mapper (Callable[[A1], A2]): mapper for element of iterable.
- `lst` *Iterable[A1]* - to map.

#### Returns

- `Iterable[A2]` - map result.

#### See also

- [A1](#a1)
- [A2](#a2)
- [hof1](#hof1)

## creducel

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L228)

```python
@hof2
def creducel(
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

## creducer

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L243)

```python
@hof2
def creducer(
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

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L192)

```python
def hof1(func: Callable[Concatenate[A1, P], AResult]):
```

Separate first argument from other.

#### See also

- [A1](#a1)
- [AResult](#aresult)
- [P](#p)

## hof2

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L204)

```python
def hof2(func: Callable[Concatenate[A1, A2, P], AResult]):
```

Separate first 2 arguments from other.

#### See also

- [A1](#a1)
- [A2](#a2)
- [AResult](#aresult)
- [P](#p)

## hof3

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L216)

```python
def hof3(func: Callable[Concatenate[A1, A2, A3, P], AResult]):
```

Separate first 3 arguments from other.

#### See also

- [A1](#a1)
- [A2](#a2)
- [A3](#a3)
- [AResult](#aresult)
- [P](#p)

## pipeline

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L143)

```python
def pipeline(func: Callable[P, Pipe[T]]) -> Callable[P, T]:
```

Decorator for functions that return [Pipe](#pipe) object for seamless unwrapping.

#### See also

- [P](#p)
- [T](#t)

## returns

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L166)

```python
def returns(x: T) -> Callable[P, T]:
```

Return `T` on any input.

#### See also

- [P](#p)
- [T](#t)

## returns_async

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L175)

```python
def returns_async(x: T) -> Callable[P, Future[T]]:
```

Return awaitable `T` on any input.

#### See also

- [P](#p)
- [T](#t)

## returns_future

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L75)

```python
def returns_future(func: Callable[P, T]):
```

Wraps  returned value of async function to [Future](#future).

#### See also

- [P](#p)
- [T](#t)

## this

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L156)

```python
def this(x: T) -> T:
```

Syncronous identity function.

#### See also

- [T](#t)

## this_async

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L161)

```python
async def this_async(x: T) -> T:
```

Asynchronous identity function.

#### See also

- [T](#t)
