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

	inputs = "strengths\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3_short(self, stdout):
		correct = 'Enter a message:\nThe first vowel is "e".\n'
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)
