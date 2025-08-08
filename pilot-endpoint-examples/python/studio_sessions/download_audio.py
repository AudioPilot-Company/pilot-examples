from dotenv import load_dotenv
from pathlib import Path
from requests import Response

import os, re, requests

load_dotenv(dotenv_path=".env.example")


API_URL = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")
API_URL += '/studio-sessions/audio/{recordId}/download'


def get_default_download_path(filename: str) -> str:
    """
    Get the default file path for downloads.
    Checks if the user's Downloads folder exists; if not, uses home directory.

    Args:
        filename (str): The filename to use.

    Returns:
        str: Full path where the file should be saved.
    """
    home = Path.home()
    downloads = home / "Downloads"
    if downloads.exists() and downloads.is_dir():
        return str(downloads / filename)
    return str(home / filename)

def get_filename_from_headers(headers) -> str:
    """
    Extract the filename from the Content-Disposition header.

    Args:
        headers (dict): The HTTP response headers.

    Returns:
        str: The extracted filename or default fallback.
    """
    content_disp = headers.get("Content-Disposition", "")
    match = re.search(r'filename="?([^"]+)"?', content_disp)
    return match.group(1) if match else "downloaded_audio.wav"

def download_audio(api_key: str, record_id: str, file_path: str = None) -> bool:
    """
    Download the audio file associated with a studio session.

    This function fetches the audio file for a given studio session record from the AudioPilot platform
    and saves it locally. If no file path is provided, it defaults to the user's Downloads folder.

    Args:
        record_id (str): The ID of the studio session record.
        api_key (str): API key with read permissions.
        file_path (str, optional): Destination path to save the file. 
                                   Defaults to the user's Downloads folder.

    Returns:
        bool: True if the download succeeds and the file is saved successfully, False otherwise.
    """
    try:
        response: Response = requests.get(
            API_URL.format(recordId=record_id),
            headers={"X-API-KEY": api_key},
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
API_KEY = "ap_abc123" # Use download API key in production
RECORD_ID = "recabc123"

download_audio(api_key=API_KEY, record_id=RECORD_ID)