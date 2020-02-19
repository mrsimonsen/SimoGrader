#files needed for testing
import pytest
import hello_world as student

def test_1():
    assert student.hello('Mr. Simonsen', 1) == 'Hello World!\nMr. Simonsen\nPeriod 1'

def test_2():
    assert student.hello('NUAMES', 14) == 'Hello World!\nNUAMES\nPeriod 14'

if __name__ == "__main__":
    print(1,"is the lonliest number, don't run tests by themselves")
