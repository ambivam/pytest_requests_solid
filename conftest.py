import pytest
import json
from src.core.service_factory import ServiceFactory

@pytest.fixture(scope="session")
def user_service():
    return ServiceFactory.get_service("user")

@pytest.fixture
def test_data():
    with open("data/test_data.json", "r") as file:
        return json.load(file)
