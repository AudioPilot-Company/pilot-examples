import requests

def get_auth_token(username: str, password: str):

    try:
        response = requests.post("https://api.audiopilot.studio/auth/tokens",
        json={"username": username, "password": password},
        headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")

    except Exception as error:
        print("Failed to fetch auth token:", error)
        return None


def upload_script(file_path: str, username: str, password: str):

    # Get authentication token
    auth_response = get_auth_token(username, password)

    if not auth_response or "token" not in auth_response:
        print("Failed to authenticate")
        return None

    access_token = auth_response["token"]["accessToken"]

    # Upload file using the retrieved access token
    try:
        with open(file_path, "rb") as file:
            files = {"file": (file_path, file, "application/pdf")}
            response = requests.post(f"https://api.audiopilot.studio/studio-sessions/script/upload-trial?externalUserId={username}",
            headers={"Authorization": f"Bearer {access_token}"},
            files=files
        )

        if response.status_code == 200:
            return response.json()

        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")


    except Exception as error:
        print("Failed to upload script:", error)
        return None

script_path = "path-to-pdf.pdf"

AUDIO_PILOT_USERNAME:str = ""
AUDIO_PILOT_PASSWORD:str = ""

# Example usage:
result = upload_script(script_path, AUDIO_PILOT_USERNAME, AUDIO_PILOT_PASSWORD)