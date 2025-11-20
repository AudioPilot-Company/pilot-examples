from models.common import BaseEntity
from models.dialogue import Dialogue
from pydantic import BaseModel
from typing import Optional, List


class SceneResponse(BaseEntity):
    id: int
    recordId: str
    voices: Optional[str] = None
    initialCharacterCount: Optional[int] = None
    coverageLogline: Optional[str] = None
    coverageGenre: Optional[str] = None
    coverageMarketability: Optional[str] = None
    coverageDemographic: Optional[str] = None
    deleted: bool = False
    dialogues: Optional[List[Dialogue]] = None


class BulkSceneUpdateResponse(BaseModel):
    sceneId: int
    success: bool
    errorMessage: Optional[str] = None
    errorCode: Optional[int] = None
    updatedScene: Optional[SceneResponse] = None


class ScenesUpdateRequest(BaseModel):
    id: int
    sceneLocationEffectsId: Optional[int] = None
    voices: Optional[str] = None
    coverageLogline: Optional[str] = None
    coverageGenre: Optional[str] = None
    coverageMarketability: Optional[str] = None
    coverageDemographic: Optional[str] = None

