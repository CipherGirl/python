import pytest
from calculator import Calculator
@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    calc = Calculator()
    assert calc.total(sample_data) == 15

def test_length(sample_data):
    assert len(sample_data) == 5