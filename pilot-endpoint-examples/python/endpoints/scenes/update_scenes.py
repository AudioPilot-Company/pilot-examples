from dotenv import load_dotenv
from typing import List
from requests import Response
import os, requests
from models.scene import ScenesUpdateRequest, BulkSceneUpdateResponse

load_dotenv(dotenv_path=".env.example")

API_URL = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")

BATCH_UPDATE_URL = f"{API_URL}/scenes/batch"


def update_scenes_batch(
    api_key: str,
    requests_payload: List[ScenesUpdateRequest]
) -> List[BulkSceneUpdateResponse]:
    """
    Batch update multiple scenes.

    Args:
        api_key (str): API key with write access.
        requests_payload (List[ScenesUpdateRequest]): List of scene update requests.

    Returns:
        List[BulkSceneUpdateResponse]: A list of update results per scene.
    """
    try:
        response: Response = requests.put(
            BATCH_UPDATE_URL,
            headers={"X-API-KEY": api_key, "Content-Type": "application/json"},
            json=[req.model_dump() for req in requests_payload]
        )
        response.raise_for_status()

        data = response.json()
        return [BulkSceneUpdateResponse(**item) for item in data]

    except Exception as error:
        print("Failed to batch update scenes:", error)
        raise

# Example usage:
API_KEY = "ap_abc123" # Use embed API key in production
scene_update_requests = [
    ScenesUpdateRequest(
        id=19671,
        sceneLocationEffectsId=9, # Ensure you use an Id from an existing SceneLocationEffect in our system
        voices='[{"character": "NARRATOR", "voice": "Ha! Ha!"}]', # Make sure to use existing Interlocutors related to the same studio session for the character field. !!!CASE SENSITIVITY MATTERS!!!
        coverageLogline="Updated logline",
        coverageGenre="Drama, Action, Thriller",
        coverageMarketability="This scene focuses on a dramatic revelation within a friendship, which can appeal to audiences who enjoy emotional and intense storytelling.",
        coverageDemographic="Comedy fans, family-oriented viewers, young adults"
    )
]

results = update_scenes_batch(API_KEY, scene_update_requests)
for result in results:
    print(result)