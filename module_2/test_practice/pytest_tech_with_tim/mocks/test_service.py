import pytest
from service import UserService, APIClient

def test_get_user_name(mocker):
    mock_api_client = mocker.Mock(spec=APIClient)

    mock_api_client.get_user_data.return_value = {"id": 1, "name": "Alice"}

    user_service = UserService(api_client=mock_api_client)

    result = user_service.get_user_name(user_id=1)

    # Name should be returned in uppercase as per UserService logic
    assert result == "ALICE"
    mock_api_client.get_user_data.assert_called_once_with(1)