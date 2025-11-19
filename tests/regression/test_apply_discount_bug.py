import pytest

def test_apply_discount_regression():
    from src.pricing import apply_discount
    result = apply_discount(100.0, 10)
    #The correct discounted price should be 90.0
    assert result == 90.0