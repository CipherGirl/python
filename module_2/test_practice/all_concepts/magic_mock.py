"""
What it is: A flexible mock object. Can mock anything.
Use when: You need a quick mock without strict signature checking.
"""

from unittest.mock import MagicMock, Mock

# Mocking a simple function
weather_api = MagicMock()
weather_api.get_weather.return_value = 25

# Using the mock
temp = weather_api.get_weather("London")
print(temp)  # 25

# Assertions
weather_api.get_weather.assert_called_once_with("London")

# Simple Mock
mock_obj = Mock()
mock_obj.method.return_value = "mocked result"
print(mock_obj.method())

# MagicMock (has magic methods implemented)
magic_mock = MagicMock()
magic_mock.__len__.return_value = 5
print(len(magic_mock))