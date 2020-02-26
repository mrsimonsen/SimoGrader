import unittest
from subprocess import run
from os import getcwd

class Tests(unittest.TestCase):
	file = "scrambler.py"
	
	def test_1(self):
		inputs = "This is my message.\n"
		correct = "What is the message to scramble?\n"
		correct += "There are 4 words in the message.\n"
		result = Tests.catchOutput(inputs)[:len(correct)]
		self.assertEqual(result, correct)
	
	def test_2(self):
		inputs = "This is my message. \n"
		correct = "What is the message to scramble?\n"
		correct += "There are 5 words in the message.\n"
		correct += "Here's the shuffeled message:\n"
		correct += "my is This  message.\n"
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