import pytest
from main import get_weather

# Mocking the requests.get method to avoid real API calls by passing 'mocker' fixture
def test_get_weather(mocker):
    mock_get = mocker.patch('main.requests.get')

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temperature": 25, "condition": "Sunny"}


    result = get_weather("Dhaka")

    assert result == {"temperature": 25, "condition": "Sunny"}
    mock_get.assert_called_once_with('http://api.weatherapi.com/v1/Dhaka')

    