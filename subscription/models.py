from typing import List

class Subscription:
    def __init__(self, repo_url: str, last_checked: str):
        self.repo_url = repo_url
        self.last_checked = last_checked

class SubscriptionManager:
    def __init__(self):
        self.subscriptions = []  # This would be loaded from a database or file

    def add_subscription(self, subscription: Subscription):
        self.subscriptions.append(subscription)

    def remove_subscription(self, repo_url: str):
        self.subscriptions = [sub for sub in self.subscriptions if sub.repo_url != repo_url]
