import pytest, random
import fortune_cookie as student

def test1():
    random.seed(2)
    assert student.cookie() == "Help! I’m being held prisoner in a fortune cookie bakery!"

def test2():
    random.seed(1)
    assert student.cookie() == "Cookie said: \"You really crack me up.\""

def test3():
    random.seed(7)
    assert student.cookie() == "You are not illiterate."

def test4():
    random.seed(0)
    assert student.cookie() == "You will read this and say \"Geez! I could come wp with better fortunes than that!\""

def test5():
    random.seed(5)
    assert student.cookie() == "This cookie is never gonna give you up, never gonna let your down."
