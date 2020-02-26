import unittest
from subprocess import run
from os import getcwd

class Tests(unittest.TestCase):
	file = "GMN2.py"
	
	def test_1(self):
		inputs = "1\n1\n1\n1\n1\n1\n1\n"
		correct = "\tWelcome to 'Guess My Number 2.0'!\n\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\n"
		result = Tests.catchOutput(inputs,'0')[:len(correct)]
		self.assertEqual(result, correct)
	
	def test_2(self):
		inputs = "1\n1\n1\n1\n1\n1\n1\n"
		correct = "\tWelcome to 'Guess My Number 2.0'!\n\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\nTake guess number 1:\n"
		result = Tests.catchOutput(inputs)[:len(correct)]
		self.assertEqual(result, correct)
	
	def test_3(self):
		inputs = "47\n"
		correct = "\tWelcome to 'Guess My Number 2.0'!\n\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\nTake guess number 1:\n"
		correct += "You guessed it! The number was 47.\nAnd it only took you 1 tries!\n"
		result = Tests.catchOutput(inputs,'0')
		self.assertEqual(result, correct)
	
	def test_4(self):
		inputs = "1\n1\n1\n1\n100\n1\n1\n"
		correct = "\tWelcome to 'Guess My Number 2.0'!\n\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\nTake guess number 1:\n"
		correct += "Higher...\nTake guess number 2:\n" 
		correct += "Higher...\nTake guess number 3:\n"
		correct += "Higher...\nTake guess number 4:\n"
		correct += "Higher...\nTake guess number 5:\n"
		correct += "Lower...\nTake guess number 6:\n"
		correct += "You ran out of tries! The number was 62.\n"
		result = Tests.catchOutput(inputs,'1')
		self.assertEqual(result, correct)
		
	# setup methods
	@staticmethod
	def catchOutput(inputs=None, seed=''):
		cwd = getcwd()
		p = run(f"python3 {Tests.file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs)
		return p.stdout

if __name__ == '__main__':
	unittest.main()