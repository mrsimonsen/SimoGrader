import pytest
import right_triangle as student

def test1():
    assert student.make_tri("@",3) == "\n@ \n@ @ \n@ @ @ \n"

def test2():
    assert student.make_tri("%", 5) == "\n% \n% % \n% % % \n% % % % \n% % % % % \n"

def test3():
    assert student.make_tri("m", 4) == "\nm \nm m \nm m m \nm m m m \n"

def test4():
    assert student.make_tri("*", 3) == "\n* \n* * \n* * * \n"
