from src.api.base_api import BaseAPI
from src.core.api_client import APIClient

class UserService(BaseAPI):
    """User API service implementing CRUD operations"""

    def __init__(self):
        super().__init__()  # Get auth token from BaseAPI
        self.api_client = APIClient(auth_token=self.auth_token)

    def create(self, payload):
        return self.api_client.request("POST", "users", json=payload)

    def get(self, user_id):
        return self.api_client.request("GET", f"users/{user_id}")

    def update(self, user_id, payload):
        return self.api_client.request("PUT", f"users/{user_id}", json=payload)

    def delete(self, user_id):
        return self.api_client.request("DELETE", f"users/{user_id}")
