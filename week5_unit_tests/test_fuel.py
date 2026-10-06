import pytest
from fuel import convert , gauge


def test_convert():
    assert convert("8459/16548") == 51
    assert convert("35/1000") == 4
    assert convert("100/100") == 100
    assert convert("0/5") == 0

def test_value_error():
    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("cat/4")
    with pytest.raises(ValueError):
        convert("4/cat")

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError) :
        convert("1/0")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(98) == "98%"      
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
