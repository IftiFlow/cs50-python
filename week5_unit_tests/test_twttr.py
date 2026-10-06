from twttr import shorten

def test_lowercase():
    assert shorten("iftikhar") == "ftkhr"
    assert shorten("onlyyours") == "nlyyrs"

def test_uppercase():
    assert shorten("IFTIKHAR") == "FTKHR"
    assert shorten("ALLUPPERCASE") == "LLPPRCS"

def test_consonants():
    assert shorten("llCnsnNts") == "llCnsnNts"
    assert shorten("Nbgs") == "Nbgs"

def test_nonletters():
    assert shorten(" !@#$%^&* 0123456789 ") == " !@#$%^&* 0123456789 "

def test_edgecases():
    assert shorten("") == ""
    assert shorten("aeiouAEIOU") == "" 




