import unittest
from subprocess import run
from os import getcwd

class Tests(unittest.TestCase):
	file = "hello_world.py"
	
	def test_1(self):
		correct = "Hello World!\n"
		result = Tests.catchOutput()[:len(correct)]
		self.assertEqual(result, correct)
		
	def test_2(self):
		correct = "Hello World!\nNUAMES\n"
		result = Tests.catchOutput()[:len(correct)]
		self.assertEqual(result, correct)
	
	def test_3(self):
		correct = "Hello World!\nNUAMES\nCS 1030\n"
		result = Tests.catchOutput()
		self.assertEqual(result, correct)

	# setup methods
	@staticmethod
	def catchOutput(inputs=None, seed=None):
		cwd = getcwd()
		p = run(f"python3 {Tests.file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs)
		return p.stdout

if __name__ == '__main__':
	unittest.main()
