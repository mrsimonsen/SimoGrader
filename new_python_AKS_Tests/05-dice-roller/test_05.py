import unittest
from subprocess import run
from os import getcwd

class Tests(unittest.TestCase):
	file = "dice_roller.py"
	
	def test_1(self):
		inputs = "5\n10\n"
		correct = "How many dice would you like to roll?\nHow many sides do the dice have?\nRolling 5x d10.\n"
		result = Tests.catchOutput(inputs)[:len(correct)]
		self.assertEqual(result, correct)
	
	def test_2(self):
		inputs = "3\n4\n"
		correct = "How many dice would you like to roll?\nHow many sides do the dice have?\nRolling 3x d4.\n"
		correct += "Roll 1: 2\nRoll 2: 1\nRoll 3: 2\n"
		result = Tests.catchOutput(inputs, '0')[:len(correct)]
		self.assertEqual(result, correct)
		
	def test_3(self):
		inputs = "3\n4\n"
		correct = "How many dice would you like to roll?\nHow many sides do the dice have?\nRolling 3x d4.\n"
		correct += "Roll 1: 2\nRoll 2: 2\nRoll 3: 1\n"
		correct += "Total: 5\n"
		result = Tests.catchOutput(inputs, '1')
		self.assertEqual(result, correct)
		
	# setup methods
	@staticmethod
	def catchOutput(inputs=None, seed=''):
		cwd = getcwd()
		p = run(f"python3 {Tests.file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs)
		return p.stdout

if __name__ == '__main__':
	unittest.main()