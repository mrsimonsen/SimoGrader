import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "some,string\nq\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1(self, stdout):
		correct = "Enter input string:\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "some,string\nq\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_2(self, stdout):
		correct = "Enter input string:\nFirst word: some\nSecond word: string\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "some,string\nanother,thing\nlast,one\nq\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3(self, stdout):
		correct = "Enter input string:\nFirst word: some\nSecond word: string\nEnter input string:\nFirst word: another\nSecond word: thing\nEnter input string:\nFirst word: last\nSecond word: one\nEnter input string:\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = " some , string  \nq\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_4(self, stdout):
		correct = "Enter input string:\nFirst word: some\nSecond word: string\nEnter input string:\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "comma_missing\nwith, two, commas\nq\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test05_part_5(self, stdout):
		correct = "Enter input string:\nError: No comma in string.\nEnter input string:\nError: Too many commas in string.\nEnter input string:\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)
