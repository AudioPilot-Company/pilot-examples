from dotenv import load_dotenv
from pathlib import Path
from requests import Response
import os, re, requests

load_dotenv(dotenv_path=".env.example")

API_URL = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")
# Updated presigned URL endpoint
API_URL += '/studio-sessions/{recordId}/presigned-url'


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


def download_audio(record_id: str, api_key: str, file_path: str = None) -> bool:
    """
    Download the audio file associated with a studio session using a presigned URL.

    Steps:
    1. Request the presigned URL for the given record ID.
    2. Download the audio from the presigned URL.

    Args:
        record_id (str): The ID of the studio session record.
        api_key (str): API key with permission to request presigned URLs.
        file_path (str, optional): Destination path to save the file. 
                                   Defaults to the user's Downloads folder.

    Returns:
        bool: True if the download succeeds, False otherwise.
    """
    try:
        # Step 1: Get presigned URL
        resp: Response = requests.get(
            API_URL.format(recordId=record_id),
            headers={"X-API-KEY": api_key}
        )
        resp.raise_for_status()
        presigned_url = resp.text.strip()  # presigned URL returned as plain string

        # Step 2: Download audio from presigned URL
        download_resp: Response = requests.get(presigned_url, stream=True)
        download_resp.raise_for_status()

        filename = get_filename_from_headers(download_resp.headers)
        if not file_path:
            file_path = get_default_download_path(filename)

        with open(file_path, "wb") as f:
            for chunk in download_resp.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        print(f"Audio downloaded successfully and saved to {file_path}")
        return True

    except Exception as e:
        print(f"Failed to download audio: {e}")
        return False

# Example usage:
API_KEY = "ap_abc123"  # Use read API key in production
RECORD_ID = "recabc123"

download_audio(record_id=RECORD_ID, api_key=API_KEY)