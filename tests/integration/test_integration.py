
import pytest
from src.pricing import bulk_total, format_currency
from src.order_io import load_order, write_receipt


def test_emptyline(tmp_path):
    p = tmp_path / "empty.csv"
    p.write_text("apple,10.00\n\nbanana,20.00", encoding="utf-8")

    items = load_order(p)

def test_malformedline(tmp_path):
    p = tmp_path / "empty.csv"
    p.write_text("apple,10.00\n\nbanana,2,0.00", encoding="utf-8")

    with pytest.raises(ValueError):
        load_order(p)

def test_order_integration(tmp_path):
    input_file = tmp_path / "order.csv"
    input_file.write_text("widget,$10.00\ngizmo,5.50\n", encoding="utf-8")
    
    items = load_order(input_file)


    assert items == [
        ("widget", 10.0),
        ("gizmo", 5.5),
    ]

    prices = [price for (_, price) in items]
    total = bulk_total(prices, discount_percent=10, tax_rate=0.07)
    
    reciept_path = tmp_path / "receipt.txt"
    write_receipt(reciept_path, items, discount_percent=10, tax_rate=0.07)
    
    output_text = reciept_path.read_text(encoding="utf-8")
    

    assert "widget: $10.00" in output_text
    assert "TOTAL:" in output_text

    expected_total = format_currency(total)
    assert expected_total in output_text
