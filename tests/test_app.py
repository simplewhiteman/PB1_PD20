import pytest
from app import check_pvn, get_total_price

def test_pvn_calculation():
    assert check_pvn(100) == 21.0

def test_pvn_zero():
    assert check_pvn(0) == 0.0

def test_pvn_negative():
    with pytest.raises(ValueError):
        check_pvn(-50)

def test_total_price():
    """Pārbauda pilnās cenas aprēķinu ar PVN."""
    assert get_total_price(100) == 121.0

    