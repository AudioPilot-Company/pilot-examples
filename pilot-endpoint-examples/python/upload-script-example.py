import requests


# Example on how to upload a script to our platform with an API key
def upload_script(file_path: str, api_key: str, external_user_id: str):
    # Upload file using API key in headers
    try:
        with open(file_path, "rb") as file:
            files = {"file": (file_path, file, "application/pdf")}
            response = requests.post(
                f"https://api.audiopilot.studio/studio-sessions/script/upload-trial?externalUserId={external_user_id}",
                headers={"X-API-KEY": api_key},
                files=files
            )

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")

    except Exception as error:
        print("Failed to upload script:", error)
        return None


# Example usage:
SCRIPT_PATH = r"C:\Users\Noah White\Downloads\girls-pilot-2-pages.pdf"
API_KEY = "ap_NNqTgU9CtLasE4RE50PRsoxxHIpyQ0jB06J6NUcigWE95YVl0BCZafisNAMNI"
EXTERNAL_USER_ID = "noah"

upload_script(SCRIPT_PATH, API_KEY, EXTERNAL_USER_ID)