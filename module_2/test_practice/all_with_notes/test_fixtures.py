import pytest
from class_calculator import Calculator

# Return instance of Calculator in every tests
@pytest.fixture
def claclulator():
    return Calculator()

# For inputs for the functionc in clacluator
@pytest.fixture
def numbers():
    return 10, 5

@pytest.fixture
def numbers_list():
    return [1, 2, 3, 4, 5]

#===============Tests=================

def test_add(calculator, numbers):
    a, b = numbers
    assert calculator.add(a, b) == 15

def test_subtract(calculator, numbers):
    a, b = numbers
    assert calculator.subtract(a, b) == 5

def test_multiply(calculator, numbers):
    a, b = numbers
    assert calculator.multiply(a, b) == 50

def test_divide(calculator, numbers):
    a, b = numbers
    assert calculator.divide(a, b) == 2

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.divide(10, 0)

def test_sum_multiple_numbers(calculator, number_list):
    assert calculator.sum(*number_list) == 15

def test_sum_no_arguments(calculator):
    assert calculator.sum() == 0