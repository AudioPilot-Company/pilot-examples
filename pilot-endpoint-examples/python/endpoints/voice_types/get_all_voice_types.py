from dotenv import load_dotenv
from models.common import Page
from models.voice_type import VoiceTypeResponse
from requests import Response
import os, requests

load_dotenv(dotenv_path=".env.example")

API_URL: str = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")

API_URL += "/voice-types/list"


def get_all_voice_types(api_key: str, page: int = 0, size: int = 20) -> Page[VoiceTypeResponse]:
    """
    Retrieve a paginated list of all voice types.

    Args:
        api_key (str): API key with read permissions.
        page (int): Page number (0-based index). Defaults to 0.
        size (int): Page size. Defaults to 20.

    Returns:
        Page[VoiceTypeResponse]: A paginated response containing voice type items.
    """
    try:
        response: Response = requests.get(
            API_URL,
            params={"page": page, "size": size},
            headers={"X-API-KEY": api_key},
        )
        response.raise_for_status()

        data = response.json()
        # Convert list of dicts → list of VoiceTypeResponse objects
        data["content"] = [VoiceTypeResponse(**item) for item in data.get("content", [])]

        return Page[VoiceTypeResponse](**data)

    except Exception as error:
        print("Failed to retrieve voice types:", error)
        raise


# Example usage:
API_KEY = "abc_123"  # Use read API key or embed API key in production

voice_types: Page[VoiceTypeResponse] = get_all_voice_types(api_key=API_KEY, page=0, size=20)
for vt in voice_types.content:
    print(vt)