import pytest
import reverse_message as student

def test1():
    assert student.reverse("This is my message") == 'egassem ym si sihT'

def test2():
    assert student.reverse("egassem ym si sihT") == "This is my message"

def test3():
    assert student.reverse("[O.o]") == "]o.O["
