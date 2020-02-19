import pytest, random
import coin_flipper as student

def test1():
    random.seed(0)
    assert student.coin(100) == (100,50,50)
def test2():
    random.seed(14)
    assert student.coin(100) == (100,58,42)
def test3():
    random.seed(14)
    assert student.coin(-100) == (0,0,0)
