from dotenv import load_dotenv
from requests import Response

import os, requests

load_dotenv(".env.example")


API_URL:str = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")
API_URL += '/studio-sessions/{recordId}'

def delete_studio_session_by_record_id(api_key: str, record_id: str) -> bool:
    """
    Delete a studio session by its record ID.

    Args:
        record_id (str): The record ID of the studio session to delete.
        api_key (str): API key with delete permissions.

    Returns:
        bool: True if the session was deleted successfully, otherwise False.
    """
    try:
        response: Response = requests.delete(
            API_URL.format(recordId=record_id),
            headers={"X-API-KEY": api_key},
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
API_KEY = "ap_abc123" # Use delete API key in production
RECORD_ID = "rec123"

delete_studio_session_by_record_id(api_key=API_KEY, record_id=RECORD_ID)