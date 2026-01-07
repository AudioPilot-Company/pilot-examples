from dotenv import load_dotenv
from models.interlocutor import InterlocutorResponse
from requests import Response
import os, requests
from typing import List, Optional

load_dotenv(dotenv_path=".env.example")

API_URL: str = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")

API_URL += "/interlocutors/search-by-record-id"


def search_interlocutors_by_record_id(
    api_key: str,
    record_id: str,
    search: Optional[str] = None
) -> List[InterlocutorResponse]:
    """
    Retrieve all interlocutors belonging to a specific record ID.

    This endpoint supports optional name-prefix searching. When `search`
    is provided, the backend returns interlocutors whose **name begins
    with the provided search string**, case-insensitive.

    Args:
        api_key (str): API key with read permissions or embed permissions.
        record_id (str): The record ID that owns the interlocutors.
        search (str | None): Optional name prefix filter.

    Returns:
        List[InterlocutorResponse]: A list of interlocutors for the given record.
    """
    try:
        response: Response = requests.get(
            API_URL,
            params={"recordId": record_id, "search": search},
            headers={"X-API-KEY": api_key},
        )
        response.raise_for_status()

        data = response.json()

        return [InterlocutorResponse(**item) for item in data]

    except Exception as error:
        print("Failed to retrieve interlocutors:", error)
        raise


# Example usage:
API_KEY = "ap_abc123" # Use read API key or embed API key in production
RECORD_ID = "recabc123"

interlocutors: List[InterlocutorResponse] = search_interlocutors_by_record_id(
    api_key=API_KEY,
    record_id=RECORD_ID
)

print(interlocutors)