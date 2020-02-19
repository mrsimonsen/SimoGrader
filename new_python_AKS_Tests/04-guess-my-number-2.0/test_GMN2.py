import pytest
import GMN2 as student

def test1():
    assert student.hi_low(1, 100, 1) == ("Low", True)

def test2():
    assert student.hi_low(100, 1, 1) == ("High", True)

def test3():
    assert student.hi_low(1, 1, 1) == ("Correct", False)

def test4():
    assert student.hi_low(100, 1, 5) == ("High", False)

def test5():
    assert student.hi_low(1, 100, 5) == ("Low", False)

def test6():
    assert student.end(5, "Correct", 14) == "You guessed it in 5 tries! The number was 14"

def test7():
    assert student.end(6, "Correct", 14) == "You ran out of tries! The number was 14"

def test8():
    assert student.end(1, "Low", 14) == "You ran out of tries! The number was 14"

def test9():
    assert student.end(1, "High", 14) == "You ran out of tries! The number was 14"
