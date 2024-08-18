import os

class Config:
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
    UPDATE_INTERVAL = 86400  # Default to daily updates (in seconds)
