from dotenv import load_dotenv
from requests import Response
from models.scene import SceneResponse
import os, requests
from typing import Optional

load_dotenv(dotenv_path=".env.example")

API_URL: str = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")

SCENE_URL = f"{API_URL}/scenes/{{id}}"


def get_scene_by_id(
    api_key: str,
    id: int
) -> Optional[SceneResponse]:
    """
    Retrieve a single scene by its unique ID.

    Args:
        api_key (str): API key with read permissions.
        id (int): The unique ID of the scene to retrieve.

    Returns:
        SceneResponse | None: The scene details if found and accessible.
    """
    try:
        response: Response = requests.get(
            SCENE_URL.format(id=id),
            headers={"X-API-KEY": api_key},
        )
        response.raise_for_status()

        data = response.json()
        return SceneResponse(**data)

    except Exception as error:
        print(f"Failed to retrieve scene {id}: {error}")
        raise


# Example usage:
API_KEY = "ap_abc123" # Use read API key or embed API key in production
SCENE_ID = 19671

scene: SceneResponse = get_scene_by_id(
    api_key=API_KEY,
    id=SCENE_ID
)

print(scene)