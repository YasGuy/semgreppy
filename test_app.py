import pytest
from app import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 2) == 8

def test_divide():
    assert divide(10, 2) == 5

    with pytest.raises(ValueError):
        divide(10, 0)
