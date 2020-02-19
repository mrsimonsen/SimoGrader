import pytest
import character_creator as student
dict = {'Strength':10,
        'Dexterity':10,
        'Constitution':10,
        'Wisdom':10,
        'Intelligence':10,
        'Charisma':10,
        'Pool':5}

def test_add1():
    sm = student.add('Wisdom', 5, dict)
    sa = dict['Wisdom']
    sp = dict['Pool']
    assert (sm,sa,sp) == ('5 added to Wisdom', 15, 0)
def test_add2():
    sm = student.add('Strength', 6, dict)
    sa = dict['Strength']
    sp = dict['Pool']
    assert (sm,sa,sp) == ('6 is more points than you have left in your pool', 10, 0)
def test_add3():
    sp = dict['Pool']
    sm = student.add('Health', 2, dict)
    assert (sm,sp) == ('Health is not a valid attribute',0)
def test_remove1():
    sm = student.remove('Intelligence', 10, dict)
    sa = dict['Intelligence']
    sp = dict['Pool']
    assert (sm,sa,sp) == ('10 removed from Intelligence', 0, 10)
def test_remove2():
    sm = student.remove('Constitution', 11, dict)
    sa = dict['Constitution']
    sp = dict['Pool']
    assert (sm,sa,sp) == ('11 is more points than you have left in Constitution', 10, 10)
def test_remove3():
    sm = student.remove('Bob', 2, dict)
    sp = dict['Pool']
    assert (sm,sp) == ('Bob is not a valid attribute',10)
def test_remove4():
    sm = student.remove('Dexterity', 5, dict)
    sa = dict['Dexterity']
    sp = dict['Pool']
    assert (sm,sa,sp) == ('5 removed from Dexterity',5,15)
def test_add4():
    sm = student.add('Charisma', 2, dict)
    sa = dict['Charisma']
    sp = dict['Pool']
    assert (sm,sa,sp) == ('2 added to Charisma',12,13)
