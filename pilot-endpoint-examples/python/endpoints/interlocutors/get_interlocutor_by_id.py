from dotenv import load_dotenv
from models.interlocutor import InterlocutorResponse
from requests import Response
import os, requests
from typing import Optional

load_dotenv(dotenv_path=".env.example")

API_URL: str = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")

API_URL += "/interlocutors/{id}"


def get_interlocutor_by_id(
    api_key: str,
    id: int
) -> Optional[InterlocutorResponse]:
    """
    Retrieve a single interlocutor by its unique ID.

    Args:
        api_key (str): API key with read permissions or embed permissions.
        id (int): The unique ID of the interlocutor to retrieve.

    Returns:
        Interlocutor | None: The interlocutor details if found and accessible.
    """
    try:
        response: Response = requests.get(
            API_URL.format(id=id),
            headers={"X-API-KEY": api_key},
        )
        response.raise_for_status()

        data = response.json()
        return InterlocutorResponse(**data)

    except Exception as error:
        print(f"Failed to retrieve interlocutor {id}: {error}")
        raise


# Example usage:
API_KEY = "ap_abc123" # Use read API key or embed API key in production
INTERLOCUTOR_ID = 12345

interlocutor:InterlocutorResponse = get_interlocutor_by_id(
    api_key=API_KEY,
    id=INTERLOCUTOR_ID
)

print(interlocutor)