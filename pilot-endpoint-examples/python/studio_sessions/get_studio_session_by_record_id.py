from dotenv import load_dotenv
from models.studio_session import StudioSession
from requests import Response

import os, requests

load_dotenv(dotenv_path=".env.example")


API_URL:str = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")
API_URL += '/studio-sessions/{recordId}'

def get_studio_session_by_record_id(record_id: str, api_key: str, user_token: str) -> StudioSession | None:
    """
    Retrieve a studio session by its record ID.

    Args:
        record_id (str): The record ID of the studio session.
        api_key (str): API key with read permissions.
        user_token (str): Token associated with the user for validation.

    Returns:
        StudioSession | None: The studio session details if found, otherwise None.
    """
    try:
        response: Response = requests.get(
            API_URL.format(recordId=record_id),
            headers={"X-API-KEY": api_key},
            params={"userToken": user_token}
        )
        response.raise_for_status()
        session:StudioSession = StudioSession(**response.json())
        print(f"Retrieved session: {session.recordId} - {session.scriptName}")
        return session

    except Exception as error:
        print("Failed to retrieve session:", error)
        return None


# Example usage:
API_KEY = "your-api-key" # Use read key in production
USER_TOKEN = "example-user-token"
RECORD_ID = "12345"

get_studio_session_by_record_id(record_id=RECORD_ID,api_key=API_KEY, user_token=USER_TOKEN)