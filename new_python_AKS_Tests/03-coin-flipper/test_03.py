import unittest
from subprocess import run
from os import getcwd

class Tests(unittest.TestCase):
	file = "coin_flipper.py"
	
	def test_1(self):
		inputs = "2\n"
		correct = "How many times do you want to flip the coin?\n"
		result = Tests.catchOutput(inputs)[:len(correct)]
		self.assertEqual(result, correct)

	def test_2(self):
		inputs = "10\n"
		correct = "How many times do you want to flip the coin?\n"
		correct += "The coin was flipped 10 times.\nHeads: 5\tTails: 5\n"
		result = Tests.catchOutput(inputs, '1')
		self.assertEqual(result, correct)
	
	def test_3(self):
		inputs = "100\n"
		correct = "How many times do you want to flip the coin?\n"
		correct += "The coin was flipped 100 times.\nHeads: 50\tTails: 50\n"
		result = Tests.catchOutput(inputs, '0')
		self.assertEqual(result, correct)
	

	# setup methods
	@staticmethod
	def catchOutput(inputs=None, seed=''):
		cwd = getcwd()
		p = run(f"python3 {Tests.file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs)
		return p.stdout

if __name__ == '__main__':
	unittest.main()