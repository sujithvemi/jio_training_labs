import pytest
from factorial import factorial

fact = factorial()
def test_factorial_float():
    with pytest.raises(TypeError):
        fact.compute(3.0)

def test_factorial_none():
    with pytest.raises(TypeError):
        fact.compute(None)

def test_factorial_neg_int():
    with pytest.raises(ValueError):
        fact.compute(-4)

def test_factorial_pos_int():
    assert fact.compute(3) == 6
    assert fact.compute(5) == 120

def test_factorial_zero():
    assert fact.compute(0) == 1