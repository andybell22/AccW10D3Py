import pytest

from sample import add, minus, divide, multiply

def test_add():
    assert add(1, 2) == 3
    assert add(14, 15) == 29
    with pytest.raises(TypeError):
        add(4, 'Three-Thousand')

def test_minus():
    assert minus(5, 3) == 2
    assert minus(6, 9) == -3
    assert minus(11, 4) != 4

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    with pytest.raises(ZeroDivisionError):
        assert divide(4, 0)

def test_multiply():
    assert multiply(3, 6) == 18