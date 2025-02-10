from abc import ABC, abstractmethod
from src.core.auth_manager import AuthManager

class BaseAPI(ABC):
    """Abstract base class for all API services"""

    def __init__(self):
        self.auth_token = AuthManager().get_token()  # Fetch auth token

    @abstractmethod
    def create(self, payload):
        pass

    @abstractmethod
    def get(self, entity_id):
        pass

    @abstractmethod
    def update(self, entity_id, payload):
        pass

    @abstractmethod
    def delete(self, entity_id):
        pass
