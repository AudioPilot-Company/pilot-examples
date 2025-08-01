from .base_entity import BaseEntity
from typing import List, Optional
from uuid import UUID


class StudioSessionResponse (BaseEntity):
    recordId: str
    status: str
    scriptId: UUID
    scriptName: str
    coverageLogline: Optional[str] = None
    coverageGenre: List[str]
    coverageMarketability: Optional[str] = None
    coverageDemographic: List[str]
    coverageDemographicExplained: Optional[str] = None
    companyId: int
    isTrial: bool
    scenesCharacterCount: Optional[int] = None
    scenesCount: Optional[int] = None
    uniqueVoicesCount: Optional[int] = None
    creditCost: int
    pages: int
    deleted: bool
    isReviewingEnabled: Optional[bool] = False
    countRegeneration: int