import pytest, random
import dice_roller as student

def test1():
    random.seed(0)
    assert student.roll(2,6) == 8

def test2():
    random.seed(14)
    assert student.roll(5,10) == 30

def test3():
    random.seed(10)
    assert student.roll(10,6) == 33
