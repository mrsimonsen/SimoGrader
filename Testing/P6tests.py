import unittest, sys, random
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "14\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1(self, stdout):
		correct = "\tWelcome to Guess My Number 2.0!\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\n"
		random.seed(14)
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "50\n10\n14\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_2(self, stdout):
		correct = "Take guess number 1:\nLower...\nTake guess number 2:\nHigher...\n"
		random.seed(14)
		student.main()
		result = stdout.getvalue()[117:len(correct)+117]
		self.assertEqual(result, correct)

	inputs = "80\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3_win(self, stdout):
		correct = "You guessed it! The number was 80.\nAnd it only took you 1 tries.\n"
		random.seed(5)
		student.main()
		result = stdout.getvalue()[-65:]
		self.assertEqual(result, correct)

	inputs = "1\n1\n1\n1\n1\n1\n1\n80\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_3_loose(self, stdout):
		correct = "You ran out of tries! The number was 80.\n"
		random.seed(5)
		student.main()
		result = stdout.getvalue()[-41:]
		self.assertEqual(result, correct)

	inputs = "1\n1\n1\n1\n1\n1\n1\n80\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test05_part_4(self, stdout):
		self.maxDiff = None
		correct = "\tWelcome to Guess My Number 2.0!\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\nTake guess number 1:\nHigher...\nTake guess number 2:\nHigher...\nTake guess number 3:\nHigher...\nTake guess number 4:\nHigher...\nTake guess number 5:\nHigher...\nTake guess number 6:\nYou ran out of tries! The number was 50.\n"
		random.seed(0)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)
