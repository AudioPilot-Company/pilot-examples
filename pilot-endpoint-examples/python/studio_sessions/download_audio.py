from dotenv import load_dotenv
from pathlib import Path
import re
from requests import Response
import os, re, requests

load_dotenv(dotenv_path=".env.example")


API_URL = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")
API_URL += '/studio-sessions/audio/{recordId}/download'


def get_default_download_path(filename: str) -> str:
    home = Path.home()
    downloads = home / "Downloads"
    if downloads.exists() and downloads.is_dir():
        return str(downloads / filename)
    return str(home / filename)

def get_filename_from_headers(headers) -> str:
    content_disp = headers.get("Content-Disposition", "")
    match = re.search(r'filename="?([^"]+)"?', content_disp)
    return match.group(1) if match else "downloaded_audio.mp3"

def download_audio(record_id: str, user_token: str, api_key: str, file_path: str = None) -> bool:
    """
    Download audio file from the AudioPilot platform.
    """
    try:
        response: Response = requests.get(
            API_URL.format(recordId=record_id),
            headers={"X-API-KEY": api_key},
            params={"userToken": user_token},
            stream=True
        )
        response.raise_for_status()

        # Determine filename
        filename = get_filename_from_headers(response.headers)
        if not file_path:
            file_path = get_default_download_path(filename)

        # Save content
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        print(f"Audio downloaded successfully and saved to {file_path}")
        return True

    except Exception as e:
        print(f"Failed to download audio: {e}")
        return False

# Example usage
RECORD_ID = "12345"
USER_TOKEN = "user-token"
API_KEY = "your-api-key-here"

download_audio(RECORD_ID, USER_TOKEN, API_KEY)