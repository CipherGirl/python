from typing import Any
import pytest
from weather import WeatherService

def test_get_weather(monkeypatch: pytest.MonkeyPatch):
    def fake_get(url: str, *args, **kwargs) -> Any:
        class FakeResponse:
            def raise_for_status(self):
                pass

            def json(self):
                return {
                    "current": {
                        "temp_c": 20.0
                    }
                }

        return FakeResponse()

    monkeypatch.setattr("requests.get", fake_get)

    service = WeatherService(api_key="test_key")
    temp = service.get_weather(city="TestCity")

    assert temp == 20.0


