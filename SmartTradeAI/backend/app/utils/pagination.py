from typing import TypeVar, Generic, Sequence
from pydantic import BaseModel
from fastapi import Query

T = TypeVar('T')

class PaginationParams:
    def __init__(
        self,
        skip: int = Query(default=0, ge=0),
        limit: int = Query(default=100, ge=1, le=100)
    ):
        self.skip = skip
        self.limit = limit

class Page(BaseModel, Generic[T]):
    items: Sequence[T]
    total: int
    skip: int
    limit: int