import unittest
from subprocess import run
from os import getcwd

class Tests(unittest.TestCase):
	file = "fortune_cookie.py"
	
	
	def test_1(self):
		correct = "You crack open your cookie and your fortune falls out:\n"
		correct += "Help! I’m being held prisoner in a fortune cookie bakery!\n"
		result = Tests.catchOutput(seed = "2")
		self.assertEqual(result, correct)

	def test_2(self):
		correct = "You crack open your cookie and your fortune falls out:\n"
		correct += "Cookie said: \"You really crack me up.\"\n"
		result = Tests.catchOutput(seed = "1")
		self.assertEqual(result, correct)
	
	def test_3(self):
		correct = "You crack open your cookie and your fortune falls out:\n"
		correct += "You are not illiterate.\n"
		result = Tests.catchOutput(seed = "7")
		self.assertEqual(result, correct)
	
	def test_4(self):
		correct = "You crack open your cookie and your fortune falls out:\n"
		correct += "You will read this and say \"Geez! I could come wp with better fortunes than that!\"\n"
		result = Tests.catchOutput(seed = "0")
		self.assertEqual(result, correct)
		
	def test_5(self):
		correct = "You crack open your cookie and your fortune falls out:\n"
		correct += "This cookie is never gonna give you up, never gonna let your down.\n"
		result = Tests.catchOutput(seed="5")
		self.assertEqual(result, correct)

	# setup methods
	@staticmethod
	def catchOutput(inputs=None, seed=None):
		cwd = getcwd()
		p = run(f"python3 {Tests.file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs)
		return p.stdout

if __name__ == '__main__':
	unittest.main()