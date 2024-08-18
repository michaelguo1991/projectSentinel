from .github_client import GitHubClient

def fetch_updates(repo_url: str):
    client = GitHubClient()
    updates = client.get_repo_updates(repo_url)
    return updates
