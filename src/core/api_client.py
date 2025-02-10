import requests
from src.utils.config_reader import ConfigReader
from src.utils.logger import Logger

class APIClient:
    """Handles API requests using Requests library"""
    
    def __init__(self, auth_token=None):
        self.base_url = ConfigReader.get("base_url")
        self.session = requests.Session()
        self.logger = Logger.get_logger()
        self.auth_token = auth_token

    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        headers = kwargs.get("headers", {})

        # Attach auth token if available
        if self.auth_token:
            headers["Authorization"] = f"Bearer {self.auth_token}"
        
        kwargs["headers"] = headers
        response = self.session.request(method, url, **kwargs)
        
        self.logger.info(f"{method} Request to {url} - Status Code: {response.status_code}")
        
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response
