from unittest.mock import patch

def fetch_data():
    import requests
    return requests.get("http://api").status_code

def test_fetch():
    with patch("employee.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        assert fetch_data() == 200
