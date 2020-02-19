#files needed for testing
import pytest
import calculator as student

def test_1():
    add = 3
    sub = -1
    mul = 2
    div = 0.5
    flr = 0
    mod = 1
    rep = f"addition is {add}\nsubtraction is {sub}\nmultiplication is {mul}\n"
    rep += f"division is {div}\nfloor division {flr}\nmodulus division is {mod}"
    assert student.math('1','2')==rep

def test_2():
    add = 17
    sub = 11
    mul = 42
    div = 4.67
    flr = 4
    mod = 2
    rep = f"addition is {add}\nsubtraction is {sub}\nmultiplication is {mul}\n"
    rep += f"division is {div}\nfloor division {flr}\nmodulus division is {mod}"
    assert student.math('14','3')==rep
