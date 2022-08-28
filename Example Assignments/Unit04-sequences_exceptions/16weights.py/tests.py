import unittest, sys, random
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "10\n30\n50\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1(self, stdout):
		correct = "Enter weight 1:\nEnter weight 2:\nEnter weight 3:\n"
		student.main(3)
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "10\n30\n50\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_2(self, stdout):
		correct = "You entered: [10.0, 30.0, 50.0]\n\n"
		student.main(3)
		result = stdout.getvalue()[48:len(correct)+48]
		self.assertEqual(result, correct)

	inputs = "10\n30\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3(self, stdout):
		correct = "Total weight: 40.0\n"
		student.main(2)
		result = stdout.getvalue()[59:len(correct)+59]
		self.assertEqual(result, correct)

	inputs = "10\n36.368\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_4(self, stdout):
		correct = "Average weight: 23.18\n"
		student.main(2)
		result = stdout.getvalue()[82:len(correct)+82]
		self.assertEqual(result, correct)

	inputs = "10\n36.368\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test05_part_5(self, stdout):
		correct = "Max weight: 36.368\n"
		student.main(2)
		result = stdout.getvalue()[104:]
		self.assertEqual(result, correct)

	inputs = "10\n25.6\na\n156.7\n350\n280.16\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test06_part_6(self, stdout):
		correct = "Enter weight 1:\nEnter weight 2:\nEnter weight 3:\nThat wasn't a number.\nEnter weight 3:\nEnter weight 4:\nEnter weight 5:\nYou entered: [10.0, 25.6, 156.7, 350.0, 280.16]\n\nTotal weight: 822.46\nAverage weight: 164.49\nMax weight: 350.0\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)


if __name__ == "__main__":
	unittest.main(module='tests', failfast=True)