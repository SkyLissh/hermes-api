from typing import Any
from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeMeta, registry

mapper_registry = registry()


class Base(metaclass=DeclarativeMeta):
    id: Any
    __abstract__ = True
    __name__: str

    registry: registry = mapper_registry
    metadata: MetaData = mapper_registry.metadata

    @classmethod
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
