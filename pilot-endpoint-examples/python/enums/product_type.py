from enum import Enum

class ProductType(Enum):
    AUDIO_PILOT = "AudioPilot"
    AUDIO_TEASER = "Audio Teaser"

    @property
    def label(self) -> str:
        return self.value