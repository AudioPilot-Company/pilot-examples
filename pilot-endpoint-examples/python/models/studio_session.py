from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID


class StudioSessionResponse(BaseModel):
    recordId: str
    status: str
    scriptId: UUID
    scriptName: str
    coverageLogline: Optional[str] = None
    coverageGenre: Optional[List[str]] = None
    coverageMarketability: Optional[str] = None
    coverageDemographic: Optional[List[str]] = None
    coverageDemographicExplained: Optional[str] = None
    companyId: int
    isTrial: bool
    scenesCharacterCount: Optional[int] = None
    scenesCount: Optional[int] = None
    uniqueVoicesCharacterCount: Optional[int] = None
    uniqueVoicesCount: Optional[int] = None
    creditCost: int
    pages: int
    deleted: bool
    isReviewingEnabled: bool = False
    countRegeneration: int
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    updatedBy: Optional[str] = None