import pytest, random
import WJ2 as student

def test_setup1():
    random.seed(0)
    W = ('one','two','three','four')
    H = ('1','2','3','4')
    assert student.setup(W, H) == ('four', 'rfuo', '4')

def test_setup2():
    random.seed(14)
    W = ('one','two','three','four')
    H = ('1','2','3','4')
    assert student.setup(W, H) == ('one', 'eon', '1')

def test_guessing1():
    assert student.guessing('bob', 'bob', 'name', False) == (False,"That's it!  You guessed it!\n",False)

def test_guessing2():
    assert student.guessing('bob', '?', 'name', False) == (True,"name",True)

def test_guessing3():
    assert student.guessing('bob', 'sue', 'name', True) == (True,"That's not it. Try again.\nType '?' if you want a hint.",True)

def test_end1():
    assert student.end(0) == "Good job not using a hint!\nThanks for playing."

def test_end2():
    assert student.end(1) == "Try to not use a hint next time.\nThanks for playing."
