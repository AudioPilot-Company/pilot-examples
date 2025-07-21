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
API_URL += '/studio-sessions/audio/{recordId}/download'

# Example on how to upload a script to our platform with an API key
def download_audio(record_id: str, file_path: str, user_token: str, api_key: str) -> bool:
    """
    Download audio file from the AudioPilot platform.

    Args:
        record_id (str): The ID of the audio record.
        file_path (str): Local file path to save the downloaded audio.
        user_token (str): User token for authentication.
        api_key (str): API key for authentication.

    Returns:
        bool: True if download successful, False otherwise.
    """
    try:
        response = requests.get(
            API_URL.format(recordId=record_id),
            headers={"X-API-KEY": api_key},
            params={"userToken": user_token},
            stream=True  # Enable streaming for large files
        )
        response.raise_for_status()

        # Save content to file in chunks to avoid memory issues with large files
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        print(f"Audio downloaded successfully and saved to {file_path}")
        return True

    except Exception as e:
        print(f"Failed to download audio: {e}")
        return False