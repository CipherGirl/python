from unittest.mock import Mock, MagicMock

# Simple Mock
mock_obj = Mock()
mock_obj.method.return_value = "mocked result"
print(mock_obj.method())  # Output: "mocked result"

# MagicMock (has magic methods implemented)
magic_mock = MagicMock()
magic_mock.__len__.return_value = 5
print(len(magic_mock))  # Output: 5