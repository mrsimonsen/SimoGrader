import unittest
from subprocess import run
from os import getcwd
from random import seed
import CC2

class Tests(unittest.TestCase):
	file = "CC2.py"
	MENU = '''
Critter Caretaker

0 - Quit
1 - Listen to your critter
2 - Feed your critter
3 - Play with your critter\n'''
	
	def test_1(self):
		seed(1)
		c = CC2.Critter('Bob')
		result = (c.hunger, c.boredom)
		correct = (2,9)
		self.assertEqual(result, correct)
		
	def test_2(self):
		seed(0)
		c = CC2.Critter('Sue')
		result = c.__str__()
		correct = "Critter Object\nName: Sue\nHunger: 6\nBoredom: 6\nMood: frustrated"
		self.assertEqual(result, correct)
	
	def test_3(self):
		self.maxDiff = None
		inputs = 'Bob\n2\n1\n3\n9\n14\n0\n'
		correct = "What do you want to name your critter?\n"
		correct += Tests.MENU + "Choice:\n"
		correct += "How much food do you want to feed your critter?\n"
		correct += "Brruppp. Thank you.\n"
		correct += Tests.MENU + "Choice:\n"
		correct += "How much fun do you and your cirtter have?\n"
		correct += "Wheee!\n"
		correct += Tests.MENU + "Choice:\n"
		correct += "Critter Object\nName: Bob\nHunger: 7\nBoredom: 1\nMood: okay\n"
		correct += Tests.MENU + "Choice:\n"
		correct += "Goodbye.\n"
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
