from main import is_prime
import pytest

@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, True),
    (4, False),
    (5, False),
    (16, False),
    (17, True),
])

def test_is_prime(number, expected):
    assert is_prime(number) == expected