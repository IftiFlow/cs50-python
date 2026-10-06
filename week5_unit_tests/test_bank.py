from bank import value

def test_hello():
    assert value("hello ,ifti") == 0

def test_h():
    assert value("hi sir") == 20
    assert value("hell SIR") == 20

def test_other_greetings():
    assert value("yo maam") == 100   

def test_case_sensitivity():
    assert value("HEllo") == 0
    assert value("HeYY Sirr") == 20

def test_starting():
    assert value("hello sir") == 0
    assert value("sir hello") == 100
    assert value("hey sir") == 20
    assert value("sir hey") == 100