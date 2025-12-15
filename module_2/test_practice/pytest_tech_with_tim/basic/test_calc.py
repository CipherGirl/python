from calc import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(5, 3) == 8
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, -1) == 0
    assert subtract(-1, 1) == -2

def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(-6, -2) == 3

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
