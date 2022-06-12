from __future__ import annotations

import copy
from dataclasses import dataclass
from functools import wraps
from typing import Awaitable, Callable, Generic, ParamSpec, TypeVar

from pymon.core import future, hof1

T = TypeVar("T")
V = TypeVar("V")


def if_some(func: Callable[[T], V]):
    """Decorator that protects function from being executed on `None` value."""

    @wraps(func)
    def _wrapper(t: T):
        match t:
            case None:
                return None
            case some:
                return func(some)

    return _wrapper


def if_none(func: Callable[[T], V]):
    """Decorator that executes some function only on `None` input."""

    @wraps(func)
    def _wrapper(t: T) -> V | None:
        match t:
            case None:
                return func(None)
            case some:
                return some

    return _wrapper


@hof1
def if_none_returns(replacement: V, value: T) -> V | T:
    """Replace `value` with `replacement` if one is `None`.

    Args:
        replacement (V): to replace with.
        value (T): to replace.

    Returns:
        V | T: some result.
    """
    match value:
        case None:
            return replacement
        case some:
            return some


@hof1
def if_some_returns(replacement: V, value: T) -> V | T:
    """Replace some `value` when it is not `None`.

    Args:
        replacement (V): to replace with.
        value (T): to replace.

    Returns:
        V | T: some result.
    """
    match value:
        case None:
            return None
        case _:
            return replacement


@hof1
def some_when(predicate: Callable[[T], bool], data: T) -> T | None:
    """Passes value next only when predicate is True, otherwise returns `None`.

    Args:
        predicate (Callable[[T], bool]): to fulfill.
        data (T): to process.

    Returns:
        T | None: result.
    """
    return data if predicate(data) else None


P = ParamSpec("P")


@dataclass(slots=True, init=False)
class choose_some(Generic[P, T]):  # noqa
    """Combines multiple sync functions into switch-case like statement.

    The first function to return non-`None` result is used. If no function passed than
    `None` is returned. Uses deepcopy to keep arguments immutable during attempts.

    Examples::

            f = (
                choose_some()
                | create_linked_node
                | create_isolated_node
            )
    """

    funcs: list[Callable[P, T | None]]

    def __init__(self) -> None:
        self.funcs = []

    def __call__(self, *args: P.args, **_: P.kwargs) -> T | None:  # noqa
        if len(self.funcs) == 0:
            return None

        for func in self.funcs:
            copy_args = copy.deepcopy(args)
            if result := func(*copy_args):
                return result

        return None

    def __or__(self, option: Callable[P, T]) -> choose_some[P, T]:
        self.funcs.append(option)
        return self


@dataclass(slots=True, init=False)
class choose_some_future(Generic[P, T]):  # noqa
    """Combines multiple sync functions into switch-case like statement.

    The first function to return non-`None` result is used. If no function passed than
    `None` is returned. Uses deepcopy to keep arguments immutable during attempts.

    Examples::

            f = (
                choose_some_future()
                | create_linked_node
                | create_isolated_node
            )
    """

    funcs: list[Callable[P, Awaitable[T | None]]]

    def __init__(self) -> None:
        self.funcs = []

    @future.returns
    async def __call__(self, *args: P.args, **_: P.kwargs) -> future[T | None]:  # noqa
        if len(self.funcs) == 0:
            return None

        for func in self.funcs:
            copy_args = copy.deepcopy(args)
            if result := await func(*copy_args):
                return result

        return None

    def __or__(self, option: Callable[P, T]) -> choose_some[P, T]:
        self.funcs.append(option)
        return self
