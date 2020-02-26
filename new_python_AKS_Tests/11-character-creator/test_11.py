import unittest
from subprocess import run
from os import getcwd

class Tests(unittest.TestCase):
	file = "character_creator.py"
	MENU = '''
\t\t ____
\t\t|Menu|
\t0 - Quit
\t1 - View Attributes and Pool
\t2 - Add to Attribute
\t3 - Remove from Attribute\n'''

	def test_1(self):
		inputs = "0\n"
		correct = MENU
		correct += "What is your choice?\n"
		correct += "Goodbye.\n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)
	
	def test_2(self):
		inputs = "1\n0\n
		correct = MENU
		correct += "What is your choice?\n"
		correct += '______________________________\nStrength\t|\t0\nDexterity\t|\t0\nConstitution\t|\t0\nWisdom\t\t|\t0\nIntelligence\t|\t0\nCharisma\t|\t0\nPool\t\t|\t72\n______________________________'
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
