from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, Integer


@as_declarative()
class Base:
    """Base class which provides automated table name
    and surrogate primary key column.
    """

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, index=True)
    __name__: str
