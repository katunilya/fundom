# Model

> Auto-generated documentation for [pymon.model](https://github.com/katunilya/pymon/blob/main/pymon/model.py) module.

- [Pymon](../README.md#-pymon) / [Modules](../MODULES.md#pymon-modules) / [Pymon](index.md#pymon) / Model
    - [Auditable](#auditable)
    - [Entity](#entity)
    - [Signed](#signed)

## Auditable

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/model.py#L27)

```python
class Auditable(Signed[TAuthor], Protocol):
```

Type that has time information about it changes.

#### See also

- [TAuthor](#tauthor)

## Entity

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/model.py#L7)

```python
class Entity(Protocol, Generic[TId]):
```

Common type for Entities in terms of Domain Driven Design.

Entity has identity and even when 2 Entities contain exactly the same data, but
differentiate in terms of identities they are considered different.

#### See also

- [TId](#tid)

## Signed

[[find in source code]](https://github.com/katunilya/pymon/blob/main/pymon/model.py#L20)

```python
class Signed(Protocol, Generic[TAuthor]):
```

Type that has information about its author.

#### See also

- [TAuthor](#tauthor)
