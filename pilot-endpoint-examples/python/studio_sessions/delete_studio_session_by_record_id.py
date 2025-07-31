from dotenv import load_dotenv
from requests import Response

import os, requests

load_dotenv(".env.example")


API_URL:str = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")
API_URL += '/studio-sessions/{recordId}'

def delete_studio_session_by_record_id(record_id: str, api_key: str, user_token: str) -> bool:
    """
    Delete a studio session by its record ID.

    Args:
        record_id (str): The record ID of the studio session to delete.
        api_key (str): API key with delete permissions.
        user_token (str): Token associated with the user for validation.

    Returns:
        bool: True if the session was deleted successfully, otherwise False.
    """
    try:
        response: Response = requests.delete(
            API_URL.format(recordId=record_id),
            headers={"X-API-KEY": api_key},
            params={"userToken": user_token}
        )
        response.raise_for_status()
        # API returns Boolean in body
        result: bool = response.json()
        print(f"Studio session with Record ID '{record_id}' deleted successfully: {result}")
        return result

    except Exception as error:
        print(f"Failed to delete session {record_id}: {error}")
        return False


# Example usage:
API_KEY = "ap_abc123" # Use delete key in production
USER_TOKEN = "example-user-token"
RECORD_ID = "rec123"

delete_studio_session_by_record_id(record_id=RECORD_ID, api_key=API_KEY, user_token=USER_TOKEN)