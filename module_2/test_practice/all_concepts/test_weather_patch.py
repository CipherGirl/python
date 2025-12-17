from weather import WeatherService
import requests
from unittest.mock import patch, MagicMock
import pytest

def test_get_weather_http_error():
    fake_response = MagicMock()
    fake_response.raise_for_status.side_effect = requests.HTTPError()

    with patch("weather.requests.get", return_value=fake_response):
        service = WeatherService("fake-key")

        with pytest.raises(requests.HTTPError):
            service.get_weather("Dhaka")


# A simple fake response class to simulate
class FakeResponse:
    def raise_for_status(self):
        pass  # simulate successful HTTP response

    def json(self):
        return {
            "current": {"temp_c": 30}
        }


def test_get_weather_without_magicmock():
    with patch("weather.requests.get", return_value=FakeResponse()) as mock_get:
        service = WeatherService("fake-key")
        temp = service.get_weather("Dhaka")

        assert temp == 30
        mock_get.assert_called_once()
