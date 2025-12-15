"""
What it is: Mock object that enforces the real interface.
Use when: You want to prevent tests from calling non-existent methods or passing wrong arguments.
"""
from unittest.mock import create_autospec

class WeatherService:
    def get_weather(self, city):
        return 20

# Create a strict mock
mock_service = create_autospec(WeatherService)

mock_service.get_weather("London")    # ✅ Works
# mock_service.get_weather()          # ❌ TypeError: missing 1 required argument
# mock_service.unknown_method()       # ❌ AttributeError
