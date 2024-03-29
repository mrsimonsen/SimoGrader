import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "Howdy\n14\n3.77\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1(self, stdout):
		correct = "Enter a string:\nEnter an integer:\nEnter a float:\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "Howdy\n14\n3.77\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_2(self, stdout):
		correct = "Enter a string:\nEnter an integer:\nEnter a float:\n"
		correct += "\nHowdy 14 3.77\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "Howdy\n14\n3.77\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3(self, stdout):
		correct = "Enter a string:\nEnter an integer:\nEnter a float:\n"
		correct += "\nHowdy 14 3.77\n"
		correct += "3.77 14 Howdy\n\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "Red Balloons\n99\n14.5\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_4(self, stdout):
		correct = "Enter a string:\nEnter an integer:\nEnter a float:\n"
		correct += "\nRed Balloons 99 14.5\n"
		correct += "14.5 99 Red Balloons\n\n"
		correct += "14.5 cast to an integer is 14.\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "Red balloons\n99\n3.14\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test05_part_5(self, stdout):
		correct = "Enter a string:\nEnter an integer:\nEnter a float:\n"
		correct += "\nRed balloons 99 3.14\n"
		correct += "3.14 99 Red balloons\n\n"
		correct += "3.14 cast to an integer is 3.\n"
		correct += "red balloons RED BALLOONS Red Balloons\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)


if __name__ == "__main__":
	unittest.main(module='tests', failfast=True)