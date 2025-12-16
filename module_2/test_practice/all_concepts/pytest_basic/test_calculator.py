from calculator import Calculator
import pytest

def test_add():
    calc = Calculator()
    assert calc.add(3, 5) == 8
    assert calc.add(-1, 1) == 0

def test_subtract():
    calc = Calculator()
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(5, 10) == -5

def test_multiply():
    calc = Calculator()
    assert calc.multiply(3, 5) == 15
    assert calc.multiply(-2, 4) == -8

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    assert calc.divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        calc.divide(10, 0)