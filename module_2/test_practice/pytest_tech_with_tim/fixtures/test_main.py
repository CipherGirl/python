import pytest
from main import UserManager

"""SETUP EXAMPLE USING FIXTURES IN PYTEST"""
"""Fixture will run before each test function to provide a fresh UserManager instance."""
@pytest.fixture
def user_manager():
    """Create a UserManager instance for testing before each test."""
    return UserManager()

# user_manager = UserManager()

def test_add_user(user_manager): # Injecting the fixture user_manager into the test function
    assert user_manager.add_user("alice","alice@email.com") == True
    assert user_manager.get_user("alice") == "alice@email.com"

def test_add_existing_user(user_manager):
    user_manager.add_user("alice","alice@email.com")
    with pytest.raises(ValueError, match="User already exists."):
        user_manager.add_user("alice","another_alice@email.com")

