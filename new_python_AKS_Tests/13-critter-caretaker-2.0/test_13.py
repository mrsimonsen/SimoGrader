import unittest
from subprocess import run
from os import getcwd

class Tests(unittest.TestCase):
	file = "CC2.py"

	def test_1(self):
		inputs = "a\n0\n"
		correct = Tests.MENU
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
