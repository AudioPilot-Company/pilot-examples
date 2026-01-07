from dotenv import load_dotenv
from models.studio_session import StudioSessionResponse
from requests import Response

import os, requests

load_dotenv(".env.example")

API_URL:str = os.getenv("API_URL")
if not API_URL:
    raise ValueError("API_URL not set in environment variables")
API_URL += '/studio-sessions/{record_id}/pay-for-trial-audio-teaser'

# Example on how to pay for a trial audio teaser with an embed key
def pay_for_trial_audio_teaser(api_key: str, record_id: str) -> StudioSessionResponse | None:
    """
    Pay for a trial audio teaser on the AudioPilot platform.

    Args:
        api_key (str): API key with embed permissions.
        record_id (str): The record ID of the trial studio session.

    Returns:
        StudioSessionResponse | None: The updated studio session details if successful, otherwise None.
    """
    try:
        response: Response = requests.post(
            API_URL.format(record_id=record_id),
            headers={"X-API-KEY": api_key}
        )

        response.raise_for_status()
        session_response: StudioSessionResponse = StudioSessionResponse(**response.json())
        print(f"Trial audio teaser payment successful. Record ID: {session_response.recordId}")
        return session_response

    except Exception as error:
        print("Failed to pay for trial audio teaser:", error)
        return None


# Example usage:
API_KEY = "ap_abc123"  # Use embed only key in production
RECORD_ID = "recabc123"     # Replace with your trial session record ID

pay_for_trial_audio_teaser(api_key=API_KEY, record_id=RECORD_ID)