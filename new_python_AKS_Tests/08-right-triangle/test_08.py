import unittest
from subprocess import run
from os import getcwd

class Tests(unittest.TestCase):
	file = "right_triangle.py"
	
	def test_1(self):
		inputs = "@\n3\n"
		correct = "Enter a character:\nEnter a triangle height:\n"
		correct += "\n@ \n@ @ \n@ @ @ \n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)
	
	def test_2(self):
		inputs = "%\n5\n"
		correct = "Enter a character:\nEnter a triangle height:\n"
		correct += "\n% \n% % \n% % % \n% % % % \n% % % % % \n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)
		
	# setup methods
	@staticmethod
def catchOutput(inputs=None, seed=None):
		cwd = getcwd()
		p = run(f"python3 {Tests.file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs)
		return p.stdout

if __name__ == '__main__':
	unittest.main()