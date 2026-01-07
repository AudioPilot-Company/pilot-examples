from enum import Enum

class CharacterType(Enum):
    CHILD_CHARACTER = "CHILD_CHARACTER"
    MAIN_CHARACTER = "MAIN_CHARACTER"
    NARRATOR = "NARRATOR"
    SIDE_CHARACTER = "SIDE_CHARACTER"

    @property
    def label(self) -> str:
        return self.value