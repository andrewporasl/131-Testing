Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
src\__init__.py       0      0   100%
src\order_io.py      20      2    90%   12, 15
src\pricing.py       26      0   100%
-----------------------------------------------
TOTAL                46      2    96%



Lines 12 and 15 are uncovered in src\order_io.py
This would be unacceptable since they still handle functions where blank spaces and malformed lines occur, so we'd need a test for that.


By adding 

def test_emptyline(tmp_path):
    p = tmp_path / "empty.csv"
    p.write_text("apple,10.00\n\nbanana,20.00", encoding="utf-8")

    items = load_order(p)

def test_malformedline(tmp_path):
    p = tmp_path / "empty.csv"
    p.write_text("apple,10.00\n\nbanana,2,0.00", encoding="utf-8")

    with pytest.raises(ValueError):
        load_order(p)


We get FULL coverage


Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
src\__init__.py       0      0   100%
src\order_io.py      20      0   100%
src\pricing.py       26      0   100%
-----------------------------------------------
TOTAL                46      0   100%