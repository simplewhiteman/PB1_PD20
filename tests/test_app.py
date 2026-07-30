import pytest
from app import check_pvn

def test_pvn_calculation():
    assert check_pvn(100) ==21.0

def test_pvn_zero():
    assert check_pvn(0) == 0.0

def test_pvn_negative():
    with pytest.raises(ValueError):
        check_pvn(-50)
    