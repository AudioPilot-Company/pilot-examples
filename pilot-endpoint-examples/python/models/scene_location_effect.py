from models.common import BaseEntity
from datetime import datetime

class SceneLocationEffectsResponse(BaseEntity):
    locationEffect: str
    sceneLocationEffectDemo: str | None = None
    sceneLocationEffects: str | None = None
    locationEffectDescription: str | None = None
