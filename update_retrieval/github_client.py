import requests
from core.config import Config

class GitHubClient:
    def __init__(self):
        self.token = Config.GITHUB_TOKEN

    def get_repo_updates(self, repo_url: str):
        headers = {'Authorization': f'token {self.token}'}
        response = requests.get(f'https://api.github.com/repos/{repo_url}/events', headers=headers)
        return response.json()
