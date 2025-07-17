import os, requests


# Example on how to upload a script to our platform with an API key
def upload_script(file_path: str, api_key: str, query_params: dict):
    try:
        with open(file_path, "rb") as file:
            files = {"file": (os.path.basename(file_path), file, "application/pdf")}
            response = requests.post(
                "https://api.audiopilot.studio/studio-sessions/script/upload",
                headers={"X-API-KEY": api_key},
                files=files,
                params=query_params
            )

        response.raise_for_status()
        return response.json()

    except Exception as error:
        print("Failed to upload script:", error)
        return None


# Example usage:
SCRIPT_PATH = r"path-to-pdf.pdf"
API_KEY = "your-api-key-here"

query_params = {
    "externalUserId": "exmaple-user-id", # ID to reference a user's studio session
    "isReviewEnabled": "true", # Enable review mode for voices and location effects
}

upload_script(SCRIPT_PATH, API_KEY, query_params)