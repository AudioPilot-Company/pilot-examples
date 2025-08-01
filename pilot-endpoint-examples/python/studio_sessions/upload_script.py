from dotenv import load_dotenv
from io import BufferedReader
from models.studio_session import StudioSessionResponse
from requests import Response
from type_dicts.upload_query_params import UploadQueryParams

import os, requests

load_dotenv(dotenv_path=".env.example")


API_URL = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")
API_URL += '/studio-sessions/script/upload'

# Example on how to upload a script to our platform with an API key
def upload_script(file_path: str, api_key: str, query_params: UploadQueryParams) -> StudioSessionResponse | None:
    """
    Upload a script to the AudioPilot platform.

    Args:
        file_path (str): Path to the script PDF file.
        api_key (str): API key with upload permissions.
        query_params (UploadQueryParams): Query parameters for the upload request.
            - externalUserId (str): Unique identifier for the user.
            - isReviewEnabled (str): "true" or "false" to enable review mode.

    Returns:
        StudioSessionResponse | None: The uploaded session details if successful, otherwise None.
    """
    
    try:
        with open(file_path, "rb") as file:
            files: dict[str, tuple[str, BufferedReader, str]] = {"file": (os.path.basename(file_path), file, "application/pdf")}
            response: Response = requests.post(
                API_URL,
                headers={"X-API-KEY": api_key},
                files=files,
                params=query_params
            )

        response.raise_for_status()
        data: dict[str, str | int | list | None] = response.json()
        session_response: StudioSessionResponse = StudioSessionResponse(**data)
        print(f"Script uploaded successfully. Record ID: {session_response.recordId}")
        return session_response

    except Exception as error:
        print("Failed to upload script:", error)
        return None


# Example usage:
SCRIPT_PATH = "path-to-pdf.pdf"
API_KEY = "ap_abc123" # Use upload only key in production

query_params: UploadQueryParams = {
    "isReviewEnabled": "true", # Enable review mode for voices and location effects
}

upload_script(SCRIPT_PATH, API_KEY, query_params)