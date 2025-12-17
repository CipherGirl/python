import os
import pytest

def get_env_var(key):
    return os.environ.get(key, "default_value")

def test_get_env_var(monkeypatch):
    # Set an environment variable
    monkeypatch.setenv("TEST_VAR", "test_value")
    
    # Test the function
    assert get_env_var("TEST_VAR") == "test_value"
    assert get_env_var("NON_EXISTENT_VAR") == "default_value"

def test_get_env_var_with_default(monkeypatch):
    # Test with no environment variable set
    assert get_env_var("NON_EXISTENT_VAR") == "default_value"

# Example of monkeypatching a function
def calculate_tax(price, tax_rate):
    return price * tax_rate

def test_calculate_tax(monkeypatch):
    # Replace the function with a mock
    mock_tax = lambda price, tax_rate: 42  # Always return 42
    monkeypatch.setattr("calculate_tax", mock_tax)
    
    # Test the mocked function
    assert calculate_tax(100, 0.2) == 42