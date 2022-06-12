from datetime import datetime
from typing import Generic, Protocol, TypeVar

TId = TypeVar("TId")


class Entity(Protocol, Generic[TId]):
    """Common type for Entities in terms of Domain Driven Design.

    Entity has identity and even when 2 Entities contain exactly the same data, but
    differentiate in terms of identities they are considered different.
    """

    uid: TId


TAuthor = TypeVar("TAuthor")


class Signed(Protocol, Generic[TAuthor]):
    """Type that has information about its author."""

    created_by: TAuthor
    updated_by: TAuthor


class Auditable(Signed[TAuthor], Protocol):
    """Type that has time information about it changes."""

    created_at: datetime
    updated_at: datetime
