import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class ConfigReader:
    """Utility to fetch environment variables"""

    @staticmethod
    def get(key, default=None):
        return os.getenv(key, default)
