from models.common import BaseEntity
from pydantic import BaseModel
from typing import Optional, Set

class VoiceTypeResponse(BaseEntity):
    id: int
    name: Optional[str]
    accent: Optional[str]
    age: Optional[str]
    description: Optional[str]
    gender: Optional[str]
    userCase: Optional[str]
    inHouseNotes: Optional[str]
    voiceId: Optional[str]
    voiceDemo: Optional[str]
    characterTypes: Optional[Set[str]]