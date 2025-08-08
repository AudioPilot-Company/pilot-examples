from dotenv import load_dotenv
from requests import Response
from models.record_access_token import RecordAccessTokenResponse

import os, requests

load_dotenv(dotenv_path=".env.example")


API_URL = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")
API_URL += '/record-access/deactivate'

def deactivate_record_secret_key(api_key: str, record_id: str) -> bool:
    """
    Deactivate an access token for a studio session on the AudioPilot platform.
    Deactivation is permanent and the token cannot be restored.

    Args:
        api_key (str): API key with embed permissions.
        record_id (str): Record ID associated with the studio session.

    Returns:
        bool: True if the key was successfully deactivated, False otherwise.
    """
    try:
        response: Response = requests.post(
            API_URL,
            headers={"X-API-KEY": api_key},
            params={"recordId": record_id} 
        )

        response.raise_for_status()
        print(f"Successfully deactivated token for record: {record_id}")
        return True

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} | Response: {response.text}")
    except Exception as err:
        print(f"Unexpected error occurred: {err}")

    return False


# Example usage:
API_KEY = "ap_abc123"  # You can pass the secret token you generated for this specific record or an embed API Key in production
RECORD_ID = "rec123"

deactivate_record_secret_key(api_key=API_KEY, record_id=RECORD_ID)