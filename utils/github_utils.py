import requests
import base64
import os

import os

# load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

PAT_TOKEN = os.getenv('GITHUB_PAT')
GITHUB_API_URL = "https://api.github.com/repos"

def fetch_file_from_github(repo_url, file_path):
    """
    Fetch a specific file content from a GitHub repository and decode it from Base64.
    """
    headers = {'Authorization': f'token {PAT_TOKEN}'}
    repo_path = '/'.join(repo_url.split('/')[-2:])  # extract owner/repo from URL
    api_url = f"{GITHUB_API_URL}/{repo_path}/contents/{file_path}"

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        file_content_base64 = response.json().get('content')
        if file_content_base64:
            file_content_decoded = base64.b64decode(file_content_base64).decode('utf-8')
            return file_content_decoded
    return None

def check_file_existence_in_repo(repo_url, file_name):
    """
    Check if a specific file exists in the root of a GitHub repository.
    """
    headers = {'Authorization': f'token {PAT_TOKEN}'}
    repo_path_segments = repo_url.split("/")
    repo_path = "/".join(repo_path_segments[-2:]) if repo_url.endswith('/') else "/".join(repo_path_segments[-2:])
    api_url = f"{GITHUB_API_URL}/{repo_path}/contents/"

    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        repo_contents = response.json()
        for item in repo_contents:
            if item['name'] == file_name:
                print(f"Found {file_name} in {repo_url}")  # @TODO remove debugging line
                return True
    else:
        print(f"Failed to access {repo_url}: {response.status_code}")  # @TODO remove debugging line
    return False
