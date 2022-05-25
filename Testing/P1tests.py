import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "1\n1\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1(self, stdout):
		correct = "Enter wall height (feet):\nEnter wall width (feet):\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "12\n15.5\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_2(self, stdout):
		correct = "Wall area: 186.0 square feet\n"
		student.main()
		result = stdout.getvalue()[51:len(correct)+51]
		self.assertEqual(result, correct)

	inputs = "12\n15.5\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3(self, stdout):
		correct = "Paint needed: 0.5314285714285715 gallons\n"
		student.main()
		result = stdout.getvalue()[80:len(correct)+80]
		self.assertEqual(result, correct)

	inputs = "14\n25\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_4(self, stdout):
		correct = "Enter wall height (feet):\nEnter wall width (feet):\n"
		correct += "Wall area: 350.0 square feet\n"
		correct += "Paint needed: 1.0 gallons\n"
		correct += "Cans needed: 1 cans\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)
