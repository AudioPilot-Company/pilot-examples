from pydantic import BaseModel
from typing import Optional, Set
from models.common import BaseEntity
from models.voice_type import VoiceType

class InterlocutorResponse(BaseEntity):
    id: int
    name: Optional[str]
    recordId: Optional[str]
    voiceType: Optional[VoiceType]
    coverageCharacterDescription: Optional[str]
    characterTypes: Optional[Set[str]]
    deleted: Optional[bool]

class InterlocutorUpdateRequest(BaseModel):
    id: int
    name: Optional[str] = None
    voiceId: Optional[str] = None
    characterType: Optional[str] = None
    coverageCharacterDescription: Optional[str] = None