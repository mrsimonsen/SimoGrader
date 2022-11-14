import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "May the force be with you!\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_2(self, stdout):
		correct = "Enter a message:\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "May the force be with you!\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_3_long(self, stdout):
		correct = 'Enter a message:\nThe first vowel is "a".\n'
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "aeiou"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3_a(self, stdout):
		correct = f'Enter a message:\nThe first vowel is "a".\n'
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)
	
	inputs = "eioua"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_3_e(self, stdout):
		correct = f'Enter a message:\nThe first vowel is "e".\n'
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "iouae"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test05_part_3_i(self, stdout):
		correct = f'Enter a message:\nThe first vowel is "i".\n'
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "ouaei"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test06_part_3_o(self, stdout):
		correct = f'Enter a message:\nThe first vowel is "o".\n'
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "uaeio"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test07_part_3_u(self, stdout):
		correct = f'Enter a message:\nThe first vowel is "u".\n'
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)


if __name__ == "__main__":
	unittest.main(module='tests', failfast=True)