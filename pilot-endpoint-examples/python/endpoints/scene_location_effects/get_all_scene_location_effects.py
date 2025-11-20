from dotenv import load_dotenv
from models.common import Page
from models.scene_location_effect import SceneLocationEffectsResponse
from requests import Response
import os, requests

# --- Load environment variables and API URL ---

load_dotenv(dotenv_path=".env.example")

API_URL = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")

SCENE_LOCATION_EFFECTS_URL = f"{API_URL}/scene-location-effects/list"

# --- Function to retrieve paginated SceneLocationEffects ---

def get_all_scene_location_effects(api_key: str, page: int = 0, size: int = 20) -> Page[SceneLocationEffectsResponse]:
    """
    Retrieve a paginated list of all SceneLocationEffects.

    Args:
        api_key (str): API key with read access.
        page (int): Page number (0-indexed). Defaults to 0.
        size (int): Page size. Defaults to 20.

    Returns:
        Page[SceneLocationEffectsResponse]: Paginated SceneLocationEffects.
    """
    try:
        response: Response = requests.get(
            SCENE_LOCATION_EFFECTS_URL,
            headers={"X-API-KEY": api_key},
            params={"page": page, "size": size}
        )
        response.raise_for_status()

        data = response.json()
        data["content"] = [SceneLocationEffectsResponse(**item) for item in data.get("content", [])]
        return Page[SceneLocationEffectsResponse](**data)

    except Exception as error:
        print("Failed to retrieve scene location effects:", error)
        raise

# --- Example usage ---

API_KEY = "ap_DkyrS1WSfBsZc4wJoALJJ1lMLjsRc1c9hEcoE9LUj4FAGBvKkViBRURibsFM7"  # Embed or read key
scene_location_effects_page = get_all_scene_location_effects(api_key=API_KEY, page=0, size=10)

for effect in scene_location_effects_page.content:
    print(effect)