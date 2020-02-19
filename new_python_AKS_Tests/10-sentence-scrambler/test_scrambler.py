import pytest, random
import scrambler as student

def test1():
    assert student.splitter("This is a message.") == (["This", 'is', 'a', 'message.'], 4)

def test2():
    assert student.splitter("This is a message. ") == (["This", 'is', 'a', 'message.', ''], 5)

def test3():
    assert student.splitter("1234") == (['1234'],1)

def test4():
    random.seed(0)
    assert student.scrambler(["This", 'is', 'a', 'message.']) == 'a This is message.'
