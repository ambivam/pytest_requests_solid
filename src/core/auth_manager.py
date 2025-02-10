import requests
from src.utils.config_reader import ConfigReader
from src.utils.logger import Logger

class AuthManager:
    """Handles authentication and token retrieval"""

    _instance = None  # Singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AuthManager, cls).__new__(cls)
            cls._instance.token = None
        return cls._instance

    def get_token(self):
        """Fetch token if not already available"""
        logger = Logger.get_logger()
        if self.token is None:
            auth_url = ConfigReader.get("auth_url")
            payload = {
                "email": ConfigReader.get("username"),
                "password": ConfigReader.get("password")
            }
            response = requests.post(auth_url, json=payload)

            if response.status_code == 200:
                self.token = response.json().get("token")
                logger.info("🔐 Authentication successful! Token received.")
            else:
                logger.error(f"❌ Authentication failed! Status Code: {response.status_code}")
        return self.token
