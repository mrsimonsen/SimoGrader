import unittest
from subprocess import run
from os import getcwd

class Tests(unittest.TestCase):
	file = "calculator.py"
	
	def test_1(self):
		inputs = "1\n2\n"
		correct = "Enter a number:\nEnter a second number:\nDoing math for 1 and 2.\n"
		result = Tests.catchOutput(inputs)[:len(correct)]
		self.assertEqual(result, correct)

	def test_2(self):
		inputs = "1\n2\n"
		correct = "Enter a number:\nEnter a second number:\nDoing math for 1 and 2.\n"
		correct += "\nAddition = 3\nSubtraction = -1\nMultiplication = 2\nExponent = 1\nDivision = 0.5\nFloor Division = 0\nModulus Division = 1\n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)
	
	def test_3(self):
		inputs = "1\n16\n"
		correct = "Enter a number:\nEnter a second number:\nDoing math for 1 and 16.\n"
		correct+="\nAddition = 17\nSubtraction = -15\nMultiplication = 16\nExponent = 1\nDivision = 0.062\nFloor Division = 0\nModulus Division = 1\n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)

	# setup methods
	@staticmethod
	def catchOutput(inputs=None, seed=''):
		cwd = getcwd()
		p = run(f"python3 {Tests.file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs)
		return p.stdout
	
if __name__ == '__main__':
	unittest.main()