import json

class ConfigReader:
    """Reads configuration from JSON files"""
    
    @staticmethod
    def get(key):
        with open("config/config.json", "r") as file:
            config = json.load(file)
        return config.get(key)
