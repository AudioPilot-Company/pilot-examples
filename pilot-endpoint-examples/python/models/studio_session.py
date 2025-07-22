from .base_entity import BaseEntity
from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

class StudioSession(BaseEntity):
    recordId: str
    status: str
    scriptId: UUID
    scriptName: str
    coverageLogline: str
    coverageGenre: List[str]
    coverageMarketability: str
    coverageDemographic: List[str]
    coverageDemographicExplained: Optional[str]
    isParsingMessageSent: bool
    isAudioGenerationMessageSent: bool
    companyId: int
    isTrial: bool
    scenesCharacterCount: int
    scenesCount: int
    uniqueVoicesCharacterCount: int
    uniqueVoicesCount: int
    creditCost: int
    pages: int
    dataSource: str
    audiopilotPackageId: Optional[int]
    deleted: bool = False
    isFromCompanyUser: bool
    isReviewingEnabled: bool = False
    countRegeneration: int = 0


class StudioSessionResponse (BaseModel):
    recordId: str
    scriptId: str
    createdAt: datetime
    updatedAt: datetime
    createdBy: str
    updatedBy: str
