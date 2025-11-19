from dotenv import load_dotenv
from models.studio_session import StudioSessionResponse
from requests import Response

import os, requests

load_dotenv(dotenv_path=".env.example")

API_URL: str = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")
API_URL += "/studio-sessions/regenerate-audiopilot"

def regenerate_audiopilot(record_id: str, api_key: str) -> StudioSessionResponse | None:
    """
    Regenerate an AudioPilot for a given studio session.

    This function triggers the AudioPilot regeneration process for the specified record ID
    on the AudioPilot platform. It returns the updated studio session response.

    Args:
        record_id (str): The ID of the studio session record.
        api_key (str): API key with permission to regenerate content.

    Returns:
        StudioSessionResponse | None: The updated studio session data if successful, otherwise None.
    """
    try:
        response: Response = requests.post(
            API_URL,
            params={"recordId": record_id},
            headers={"X-API-KEY": api_key}
        )

        response.raise_for_status()
        session: StudioSessionResponse = StudioSessionResponse(**response.json())
        print(f"Regenerated AudioPilot for session: {session.recordId} - {session.scriptName}")
        return session

    except Exception as error:
        print("Failed to regenerate AudioPilot:", error)
        return None


# Example usage:
API_KEY = "ap_abc123"  # Use regenerate API key in production
RECORD_ID = "recabc123"

regenerate_audiopilot(record_id=RECORD_ID, api_key=API_KEY)