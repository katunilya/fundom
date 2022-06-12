from typing import Generic, Protocol, TypeVar

TId = TypeVar("TId")


class Entity(Protocol, Generic[TId]):
    """Common type for Entities in terms of Domain Driven Design.

    Entity has identity and even when 2 Entities contain exactly the same data, but
    differentiate in terms of identities they are considered different.
    """

    uid: TId
