import unittest
from subprocess import run
from os import getcwd

class Tests(unittest.TestCase):
	file = "counter.py"
	
	def test_1(self):
		inputs = "1\n10\n2\n"
		correct = "What is the starting number?\nWhat is the ending number?\nHow much should I count by?\nCounting from 1 to 10 by 2:"
		result = Tests.catchOutput(inputs)[:len(correct)]
		self.assertEqual(result, correct)
		
	def test_2(self):
		inputs = "1\n10\n2\n"
		correct = "What is the starting number?\nWhat is the ending number?\nHow much should I count by?\nCounting from 1 to 10 by 2:\n"
		correct += "1 3 5 7 9 \n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)
		
	def test_3(self):
		inputs = "3\n1\n-1\n"
		correct = "What is the starting number?\nWhat is the ending number?\nHow much should I count by?\nCounting from 3 to 1 by -1:\n"
		correct += "3 2 1 \n"
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