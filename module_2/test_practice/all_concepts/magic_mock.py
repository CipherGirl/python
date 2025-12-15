"""
What it is: A flexible mock object. Can mock anything.
Use when: You need a quick mock without strict signature checking.
"""

from unittest.mock import MagicMock

# Mocking a simple function
weather_api = MagicMock()
weather_api.get_weather.return_value = 25

# Using the mock
temp = weather_api.get_weather("London")
print(temp)  # 25

# Assertions
weather_api.get_weather.assert_called_once_with("London")
