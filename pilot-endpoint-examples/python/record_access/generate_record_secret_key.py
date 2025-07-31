from dotenv import load_dotenv
from requests import Response
from models.record_access_token import RecordAccessTokenResponse

import os, requests

load_dotenv(dotenv_path=".env.example")


API_URL = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")
API_URL += '/record-access/generate-secret-key'


def generate_record_secret_key(api_key: str, record_id: str) -> RecordAccessTokenResponse | None:
    """
    Generates a temporary access token to view a specific record via embed. If a new key is generated the old key is deactivated.

    Args:
        api_key (str): The API key provided to your company (with embed access).
        record_id (str): The ID of the record you wish to embed.

    Returns:
        RecordAccessTokenResponse | None: Token details if the request is successful, otherwise None.
    """
    try:
        response: Response = requests.post(
            API_URL,
            headers={"X-API-KEY": api_key},
            json={"recordId": record_id}
        )

        response.raise_for_status()
        data: dict = response.json()
        token_response = RecordAccessTokenResponse(**data)

        print(f"Token generated for record: {token_response.recordId}")
        return token_response

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} | Response: {response.text}")
    except Exception as err:
        print(f"Unexpected error occurred: {err}")

    return None

# Example usage:
API_KEY = "ap_JBh4EfVAxgz7cmvhx1Q8YWOSfLVZKOIrukO1hJaoeJtQdeiF5JD9WechgzpgQ" # Use embed only key in production
RECORD_ID = "recYC70jXOEuZ9RRLwAg"

generate_record_secret_key(API_KEY, RECORD_ID)