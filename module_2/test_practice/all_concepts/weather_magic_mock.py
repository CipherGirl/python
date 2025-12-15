from typing import Any
from unittest.mock import MagicMock

import pytest

from weather import WeatherService

def test_get_weather(monkeypatch: pytest.MonkeyPatch):
    def fake_get(url: str, *args, **kwargs) -> Any:
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "current": {
                "temp_c": 20.0
            }
        }
        return mock_response

    monkeypatch.setattr("requests.get", fake_get)

    service = WeatherService(api_key="test_key")
    temp = service.get_weather(city="TestCity")

    assert temp == 20.0


