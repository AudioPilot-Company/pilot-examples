from datetime import datetime
from typing import Generic, List, Optional, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class AuditBase(BaseModel):
    """
    Common audit fields for all entities.
    """
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    updatedBy: Optional[str] = None


class BaseEntity(AuditBase):
    """
    Base entity with ID and audit fields.
    """
    id: Optional[int] = None

class SortInfo(BaseModel):
    empty: Optional[bool] = None
    sorted: Optional[bool] = None
    unsorted: Optional[bool] = None

class Pageable(BaseModel):
    """
    Metadata about the page request.

    Attributes:
        sort (SortInfo | None): Sorting information for the page.
        offset (int | None): Offset index of the first element on the page.
        pageNumber (int | None): Current page number (0-based index).
        pageSize (int | None): Number of elements per page.
        paged (bool | None): True if the request is paged.
        unpaged (bool | None): True if the request is unpaged.
    """
    sort: Optional[SortInfo] = None
    offset: Optional[int] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None
    paged: Optional[bool] = None
    unpaged: Optional[bool] = None

class Page(BaseModel, Generic[T]):
    """
    Generic model for paginated responses.

    Attributes:
        content (List[T]): List of items on the current page.
        pageable (Pageable | None): Page request metadata.
        last (bool | None): True if this is the last page.
        totalPages (int | None): Total number of pages.
        totalElements (int | None): Total number of elements across all pages.
        size (int | None): Number of items per page.
        number (int | None): Current page number (0-based index).
        sort (SortInfo | None): Sorting information for the page.
        numberOfElements (int | None): Number of elements on this page.
        first (bool | None): True if this is the first page.
        empty (bool | None): True if this page has no content.
    """
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