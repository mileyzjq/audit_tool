import requests
import base64
import os
from git import Repo
from dotenv import load_dotenv
import sys

load_dotenv()

# Fetch the access token from the environment
access_token = os.getenv("ACCESS_TOKEN")
organization = os.getenv("ORGANIZATION")
readme_file = os.getenv("REPORT_MARKDOWN")
report_file = os.getenv("REPORT_FILE")
base_url = os.getenv("BASE_URL")

def write_files_to_github(access_token, repo, file_path):
    url = f"{base_url}/repos/{organization}/{repo}/contents/{file_path}"
    print(url)
    # Headers for authentication
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Read the content of the README file
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            file_content = file.read()
    else:
        print(f"File {file_path} does not exist.")
        return

    # Create the request payload
    payload = {
        "message": f"Update {file_path}",
        "content": file_content
    }

    # Encode the content as Base64
    encoded_content = base64.b64encode(file_content).decode()
    payload["content"] = encoded_content

    # Get the current README file SHA
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        current_readme = response.json()
        payload["sha"] = current_readme["sha"]

    # Create or update the README file
    response = requests.put(url, headers=headers, json=payload)

    if response.status_code == 200:
        print(f"{file_path} successfully written to GitHub repository.")
    else:
        print(f"Error occurred while writing {file_path}:", response.status_code)
        print(f"Error occurred: ", response.json())


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # repo = f'report-{sys.argv[1]}'
        repo = 'report-xwinner-platform-contracts'
        #write_files_to_github(access_token, repo, readme_file)
        #send_images_to_repo(repo, 'Picture1.png')
        #write_files_to_github(access_token, repo, 'Picture1.png')
        write_files_to_github(access_token, repo, 'README.pdf')
    else:
        print("No input value provided.")