import pytest

@pytest.mark.critical
def test_create_user(user_service, test_data):
    """Verify user creation"""
    response = user_service.create(test_data["new_user"])
    assert response.status_code == 201
    assert response.json()["name"] == test_data["new_user"]["name"]

@pytest.mark.regression
def test_get_user(user_service):
    """Verify fetching user details"""
    response = user_service.get(2)
    assert response.status_code == 200
    assert "data" in response.json()

@pytest.mark.smoke
def test_update_user(user_service, test_data):
    """Verify updating user details"""
    response = user_service.update(2, test_data["updated_user"])
    assert response.status_code == 200
    assert response.json()["job"] == test_data["updated_user"]["job"]

@pytest.mark.negative
def test_delete_user(user_service):
    """Verify deleting a user"""
    response = user_service.delete(2)
    assert response.status_code == 204
