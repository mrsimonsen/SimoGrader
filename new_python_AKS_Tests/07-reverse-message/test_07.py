import unittest
from subprocess import run
from os import getcwd

class Tests(unittest.TestCase):
	file = "reverse_message.py"
	
	def test_1(self):
		inputs = "This is my message."
		correct = "What is your message?\n\nYour message reversed is:\n"
		correct += ".egassem ym si sihT\n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)
	
	def test_2(self):
		inputs = "With some   space   . "
		correct = "What is your message?\n\nYour message reversed is:\n"
		correct += " .   ecaps   emos htiW\n"
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