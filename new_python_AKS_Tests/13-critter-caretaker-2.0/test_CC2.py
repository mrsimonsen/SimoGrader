import pytest, random
from CC2 import Critter as C



def test_talk1():
    random.seed(14)
    a = C('bob')
    assert a.talk() == "I'm bob and I feel okay now.\n"

def test_talk2():
    random.seed(0)
    a = C('bob')
    assert a.talk() == "I'm bob and I feel frustrated now.\n"

def test_eat1():
    random.seed(14)
    a = C('bob')
    assert a.eat(10) == "Brruppp.  Thank you." and a.hunger == 1

def test_eat2():
    random.seed(0)
    a = C('bob')
    a.eat(5)
    assert a.hunger == 2

def test_play1():
    random.seed(14)
    a = C('bob')
    assert a.play(10) == "Wheee!" and a.boredom == 1

def test_play2():
    random.seed(0)
    a = C('bob')
    a.play(5)
    assert a.boredom == 2

def test_str1():
    random.seed(14)
    a = C('bob')
    assert a.__str__() == f'Critter Object\nName: bob\nHunger: 1\nBoredom: 9\nMood: okay\n'

def test_str2():
    random.seed(0)
    a = C('sue')
    assert a.__str__() == f'Critter Object\nName: sue\nHunger: 6\nBoredom: 6\nMood: frustrated\n'
