from pydantic import BaseModel
from typing import Optional, Set
from models.voice_type import VoiceType

class Interlocutor(BaseModel):
    id: int
    name: Optional[str]
    recordId: Optional[str]
    voiceType: Optional[VoiceType]
    coverageCharacterDescription: Optional[str]
    characterTypes: Optional[Set[str]]
    deleted: Optional[bool]