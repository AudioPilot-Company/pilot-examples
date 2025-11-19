from dotenv import load_dotenv
from enums.character_type import CharacterType
from models.interlocutor import InterlocutorResponse, InterlocutorUpdateRequest
from requests import Response
import os, requests

load_dotenv(dotenv_path=".env.example")

API_URL: str = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")

API_URL += "/interlocutors"

def update_interlocutor(
    api_key: str,
    request: InterlocutorUpdateRequest
) -> InterlocutorResponse:
    """
    Update an existing interlocutor.

    Only the fields provided in the request object will be updated.
    Fields that are None will be ignored. Special logic applies to
    `voiceId`: if provided and different from the current voiceType,
    the interlocutor's voiceType will be updated.

    Args:
        api_key (str): API key with write permissions.
        request (InterlocutorUpdateRequest): The ID of the interlocutor
            and the fields to update.

    Returns:
        InterlocutorResponse: The updated interlocutor object.
    """
    try:
        response: Response = requests.put(
            API_URL,
            json=request.dict(exclude_unset=True),  # Only send fields that are set
            headers={"X-API-KEY": api_key},
        )
        response.raise_for_status()

        data = response.json()
        return InterlocutorResponse(**data)

    except Exception as error:
        print(f"Failed to update interlocutor {request.id}: {error}")
        raise


# Example usage:
API_KEY = "ap_abc123"  # Use write API key in production
UPDATE_REQUEST: InterlocutorUpdateRequest = InterlocutorUpdateRequest(
    id=13948,
    name="Updated NARRATOR",
    voiceId="NEW_VOICE_ID",
    characterType=CharacterType.NARRATOR.value,
    coverageCharacterDescription="Updated description"
)

updated_interlocutor: InterlocutorResponse = update_interlocutor(
    api_key=API_KEY,
    request=UPDATE_REQUEST
)

print(updated_interlocutor)