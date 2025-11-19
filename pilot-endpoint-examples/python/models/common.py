from typing import Generic, List, Optional, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class SortInfo(BaseModel):
    empty: Optional[bool] = None
    sorted: Optional[bool] = None
    unsorted: Optional[bool] = None

class Pageable(BaseModel):
    sort: Optional[SortInfo] = None
    offset: Optional[int] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None
    paged: Optional[bool] = None
    unpaged: Optional[bool] = None

class Page(BaseModel, Generic[T]):
    content: List[T]
    pageable: Optional[Pageable] = None
    last: Optional[bool] = None
    totalPages: Optional[int] = None
    totalElements: Optional[int] = None
    size: Optional[int] = None
    number: Optional[int] = None
    sort: Optional[SortInfo] = None
    numberOfElements: Optional[int] = None
    first: Optional[bool] = None
    empty: Optional[bool] = None