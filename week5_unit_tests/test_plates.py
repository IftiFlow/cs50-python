from plates import is_valid

def test_starting():
    assert is_valid("5cs50") == False
    assert is_valid("C250") == False
    assert is_valid("Il832") == True
    assert is_valid("sr") == True

def test_numbers():
    assert is_valid("AA567i") == False
    assert is_valid("isF1l3") == False
    assert is_valid("in02") == False
    assert is_valid("oo12") == True
    assert is_valid("aa110") == True

def test_charcount():
    assert is_valid("aa98722") == False
    assert is_valid("a") == False
    assert is_valid("AI") == True
    assert is_valid("aa1102") == True

def test_specialchar():
    assert is_valid("AI:_12") == False
    assert is_valid("ai 11") == False
    assert is_valid("AI11") == True