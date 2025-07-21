from dotenv import load_dotenv
from pathlib import Path
from requests import Response
import platform

import os, requests

load_dotenv(dotenv_path=".env.example")


API_URL = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")
API_URL += '/studio-sessions/audio/{recordId}/download'


def get_default_download_path(filename: str) -> str:
    home = Path.home()

    # Cross-platform Downloads folder heuristics
    if platform.system() == "Windows":
        downloads = home / "Downloads"
    elif platform.system() == "Darwin":  # macOS
        downloads = home / "Downloads"
    else:
        # For Linux, common default, but could vary
        downloads = home / "Downloads"

    # Ensure Downloads folder exists or fallback to home
    if downloads.exists() and downloads.is_dir():
        return str(downloads / filename)
    else:
        return str(home / filename)


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
        response:Response = requests.get(
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
    
RECORD_ID = "12345"
USER_TOKEN = "user-token"
API_KEY = "your-api-key-here"
OUTPUT_PATH = get_default_download_path(RECORD_ID)

download_audio(RECORD_ID, OUTPUT_PATH, USER_TOKEN, API_KEY)