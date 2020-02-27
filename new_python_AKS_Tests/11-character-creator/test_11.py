import unittest
from subprocess import run
from os import getcwd
import character_creator

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
		correct += ''' ______________________________
Strength\t|\t0
Dexterity\t|\t0
Constitution\t|\t0
Wisdom\t\t|\t0
Intelligence\t|\t0
Charisma\t|\t0
Pool\t\t|\t72
______________________________'''
		result = Tests.catchOutput(inputs, '0')
		self.assertEqual(result, correct)
	
	def test_3(self):
		test_dict = {'Something': 0,
					 'Another': 0,
					 'Pool': 10}
		#############################
		#https://stackoverflow.com/questions/9829331/how-do-i-handle-multiple-asserts-within-a-single-python-unittest
		##################
		correct = "5 added to Something"
		result = character_creator.add('Something', 5, test_dict)
		self.assertEqual(result, correct)
		correct = "15 is more points than you have left in Something"
		
# setup methods
	@staticmethod
	def catchOutput(inputs=None, seed=''):
		cwd = getcwd()
		p = run(f"python3 {Tests.file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs)
		return p.stdout

if __name__ == '__main__':
	unittest.main()
