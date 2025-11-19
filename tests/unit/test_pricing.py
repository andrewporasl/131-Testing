import pytest
from src.pricing import parse_price, format_currency, bulk_total, apply_discount, add_tax
from src.order_io import load_order, write_receipt
@pytest.fixture
def price():
    return 10.0

@pytest.mark.parametrize("text, expected", [
   ("$1,234.50", 1234.50),
   ("$12.5", 12.5),
   ("$0.99", 0.99),
])
def test_parse_price(text, expected):
    assert parse_price(text) == expected

@pytest.mark.parametrize("invalid_text", [
    "", "abc", "$12,34,56"
])
def test_parse_price_invalid(invalid_text):
    with pytest.raises(ValueError):
        parse_price(invalid_text)

@pytest.mark.parametrize("value, expected", [
    (10.0, "$10.00"),
    (0, "$0.00"),
    (12.345, "$12.35"),
])
def test_format_currency(value, expected):
    assert format_currency(value) == expected

def test_apply_discount(price):
    assert apply_discount(price, 0) == price

def test_apply_discount_negative(price):
    with pytest.raises(ValueError):
        apply_discount(price, -1)

def test_apply_discount_100(price):
    assert apply_discount(price, 100) == 0


def test_add_tax_default(price):
    assert add_tax(price) == price * (1.07)

def test_add_tax_custom(price):
    assert add_tax(price, 0.1) == price * (1.1)

def test_add_tax_negative(price):
    with pytest.raises(ValueError):
        add_tax(price, -1)

def test_bulk_total():
    prices = [1, 2, 3]
    assert bulk_total(prices) == pytest.approx(6 * 1.07)
