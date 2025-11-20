from dotenv import load_dotenv
from requests import Response
import os, requests
from models.scene import ScenesUpdateRequest, SceneResponse
from typing import Optional

load_dotenv(dotenv_path=".env.example")

API_URL = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")

SINGLE_UPDATE_URL = f"{API_URL}/scenes"  # your PUT mapping endpoint


def update_scene(
    api_key: str,
    request_payload: ScenesUpdateRequest
) -> Optional[SceneResponse]:
    """
    Update a single scene.

    Args:
        api_key (str): API key with write access.
        request_payload (ScenesUpdateRequest): Scene update request.

    Returns:
        SceneResponse | None: The updated scene object.
    """
    try:
        response: Response = requests.put(
            SINGLE_UPDATE_URL,
            headers={"X-API-KEY": api_key, "Content-Type": "application/json"},
            json=request_payload.model_dump()  # Pydantic V2 method
        )
        response.raise_for_status()

        data = response.json()
        return SceneResponse(**data)

    except Exception as error:
        print(f"Failed to update scene {request_payload.id}:", error)
        raise


# Example usage:
API_KEY = "ap_abc123"

scene_update_request = ScenesUpdateRequest(
    id=19671,
    sceneLocationEffectsId=9,  # Ensure you use an Id from an existing SceneLocationEffect in our system
    voices='[{"character": "NARRATOR", "voice": "Ha! Ha!"}]',
    coverageLogline="Updated logline",
    coverageGenre="Drama, Action, Thriller",
    coverageMarketability="This scene focuses on a dramatic revelation within a friendship...",
    coverageDemographic="Comedy fans, family-oriented viewers, young adults"
)

updated_scene: SceneResponse = update_scene(API_KEY, scene_update_request)
print(updated_scene)