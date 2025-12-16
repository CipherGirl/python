import pytest
from unittest.mock import Mock
from user_service import UserService


def test_get_user_name():
    # Create a mock database service
    mock_db = Mock()
    mock_db.get_user.return_value = {"id": 1, "name": "Hena"}

    #User service with mocked db
    user_service = UserService(mock_db)

    name = user_service.get_user_name(1)

    assert name == "Hena"

    mock_db.get_user.assert_called_once_with(1)