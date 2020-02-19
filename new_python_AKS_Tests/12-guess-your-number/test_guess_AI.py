import pytest
import guess_AI as student

def test1():
    assert student.high_low(1,100,50,'correct',1,True) == (1,100,1,False)

def test2():
    assert student.high_low(1,100,20,'low',1,True) == (21,100,2,True)

def test3():
    assert student.high_low(1,100,50,'high',6,True) == (1,100,6,False)

def test4():
    assert student.end(4,'correct') == "I knew I could beat you, and in 4 tries too!"

def test5():
    assert student.end(6,'correct') == "I knew I could beat you, and in 6 tries too!"

def test6():
    assert student.end(7, 'correct') == "I ran out of tries! You bested me!"

def test7():
    assert student.end(1,'high') == "I ran out of tries! You bested me!"
