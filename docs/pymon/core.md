# Core

> Auto-generated documentation for [pymon.core](https://github.com/katunilya/pymon/blob/main/pymon/core.py) module.

- [Pymon](../README.md#-pymon) / [Modules](../MODULES.md#pymon-modules) / [Pymon](index.md#pymon) / Core
    - [Func](#func)
    - [FutureFunc](#futurefunc)
    - [future](#future)
    - [pipe](#pipe)
        - [pipe().finish](#pipefinish)
    - [cfilter](#cfilter)
    - [cmap](#cmap)
    - [foldl](#foldl)
    - [foldr](#foldr)
    - [func](#func)
    - [future_func](#future_func)
    - [hof1](#hof1)
    - [hof2](#hof2)
    - [hof3](#hof3)
    - [pipeline](#pipeline)
    - [returns](#returns)
    - [returns_async](#returns_async)
    - [returns_future](#returns_future)
    - [this](#this)
    - [this_async](#this_async)

## Func

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L163)

```python
dataclass(slots=True, frozen=True)
class Func(Generic[P, V]):
```

Function composition abstraction.

#### See also

- [P](#p)
- [V](#v)

## FutureFunc

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L141)

```python
dataclass(slots=True, frozen=True)
class FutureFunc(Generic[P, V]):
```

Abstraction over async function.

#### See also

- [P](#p)
- [V](#v)

## future

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L23)

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

## pipe

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L69)

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

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L90)

```python
def finish() -> T:
```

Finish [pipe](#pipe) by unpacking internal value.

#### Returns

- `T` - internal value

#### See also

- [T](#t)

## cfilter

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L285)

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

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L271)

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

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L241)

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

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L256)

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

## func

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L184)

```python
def func(func: Callable[P, V]) -> Func[P, V]:
```

Decorator for making functions composable.

#### See also

- [P](#p)
- [V](#v)

## future_func

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L189)

```python
def future_func(func: Callable[P, Awaitable[V]]) -> FutureFunc[P, V]:
```

Decorator for making async functions composable.

#### See also

- [P](#p)
- [V](#v)

## hof1

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L202)

```python
def hof1(f: Callable[Concatenate[A1, P], AResult]):
```

Separate first argument from other.

#### See also

- [A1](#a1)
- [AResult](#aresult)
- [P](#p)

## hof2

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L215)

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

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L228)

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

## pipeline

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L99)

```python
def pipeline(func: Callable[P, pipe[T]]) -> Callable[P, T]:
```

Decorator for functions that return `Pipe` object for seamless unwrapping.

#### See also

- [P](#p)
- [T](#t)

## returns

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L122)

```python
def returns(x: T) -> Callable[P, T]:
```

Return `T` on any input.

#### See also

- [P](#p)
- [T](#t)

## returns_async

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L131)

```python
def returns_async(x: T) -> Callable[P, future[T]]:
```

Return awaitable `T` on any input.

#### See also

- [P](#p)
- [T](#t)

## returns_future

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L54)

```python
def returns_future(func: Callable[P, T]):
```

Wraps returned value of async function to [future](#future).

#### See also

- [P](#p)
- [T](#t)

## this

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L112)

```python
def this(x: T) -> T:
```

Synchronous identity function.

#### See also

- [T](#t)

## this_async

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/core.py#L117)

```python
async def this_async(x: T) -> T:
```

Asynchronous identity function.

#### See also

- [T](#t)
