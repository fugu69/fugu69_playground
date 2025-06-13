import pytest
from task1.solution import strict

@strict
def add(a: int, b: float):
    return a + b

def test_valid_args():
    assert add(3, 4.5) == 7.5

def test_invalid_int():
    with pytest.raises(TypeError, match="Argument 'a' must be int"):
        add("3", 4.5)

def test_invalid_float():
    with pytest.raises(TypeError, match="Argument 'b' must be float"):
        add(3, "4.5")

def test_invalid_both():
    with pytest.raises(TypeError, match="Argument 'a' must be int"):
        add("3", "4.5")