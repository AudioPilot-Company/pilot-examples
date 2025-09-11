from enum import Enum

class ProductType(Enum):
    AUDIO_PILOT = "AUDIO_PILOT"
    AUDIO_TEASER = "AUDIO_TEASER"

    @property
    def label(self) -> str:
        return self.value