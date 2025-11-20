from dotenv import load_dotenv
from typing import List
from requests import Response
from models.common import Page
from models.scene import SceneResponse
import os, requests

load_dotenv(dotenv_path=".env.example")

API_URL = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")

SCENES_URL = f"{API_URL}/scenes/search-by-record-id"


def search_scenes_by_record_id(api_key: str, record_id: str, page: int = 0, size: int = 20) -> Page[SceneResponse]:
    """
    Retrieve scenes associated with a record ID.
    """
    try:
        response: Response = requests.get(
            SCENES_URL,
            params={"page": page, "size": size, "recordId": record_id},
            headers={"X-API-KEY": api_key},
        )
        response.raise_for_status()

        data = response.json()

        # Convert list of dicts → list of SceneResponse objects
        data["content"] = [SceneResponse(**item) for item in data.get("content", [])]

        return Page[SceneResponse](**data)

    except Exception as error:
        print("Failed to retrieve scenes:", error)
        raise

# Example usage:
API_KEY = "ap_abc123"  # Use read API key or embed API key in production
RECORD_ID = "recwEBGmr3yKcbiMMd8C"
scenes: Page[SceneResponse] = search_scenes_by_record_id(api_key=API_KEY, record_id=RECORD_ID, page=0, size=20)
for s in scenes.content:
    print(s)