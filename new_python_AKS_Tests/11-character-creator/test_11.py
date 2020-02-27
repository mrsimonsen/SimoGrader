import unittest
from subprocess import run
from os import getcwd
import character_creator

class Tests(unittest.TestCase):
	file = "character_creator.py"
	MENU = '''
\t\t\t ____
\t\t\t|Menu|
\t\t0 - Quit
\t\t1 - View Attributes and Pool
\t\t2 - Add to Attribute
\t\t3 - Remove from Attribute\n'''

	def test_1(self):
		inputs = "a\n0\n"
		correct = Tests.MENU
		correct += "What's your choice?\n"
		correct += "'a' is not a valid menu option.\n"
		correct += Tests.MENU
		correct += "What's your choice?\n"
		correct += "Goodbye.\n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)
	
	def test_2(self):
		with self.subTest():
			inputs = "1\n0\n"
			correct = Tests.MENU
			correct += "What's your choice?\n"
			correct += '''
______________________________
Strength\t|\t0
Dexterity\t|\t0
Constitution\t|\t0
Wisdom\t\t|\t0
Intelligence\t|\t0
Charisma\t|\t0
Pool\t\t|\t72
______________________________\n'''
			correct += Tests.MENU
			correct += "What's your choice?\n"
			correct += "Goodbye.\n"
			result = Tests.catchOutput(inputs, '0')
			self.assertEqual(result, correct)
		with self.subTest():
			test_dict = {
				'Strength':10,
				'Dexterity':10,
				'Constitution':10,
				'Wisdom':10,
				'Intelligence':10,
				'Charisma': 10,
				'Pool':2}
			correct = '''
______________________________
Strength\t|\t10
Dexterity\t|\t10
Constitution\t|\t10
Wisdom\t\t|\t10
Intelligence\t|\t10
Charisma\t|\t10
Pool\t\t|\t2
______________________________'''
			result = character_creator.table(test_dict)
			self.assertEqual(result, correct)
	
	def test_3(self):
		test_dict = {'Something': 0,
					 'Pool': 10}
		with self.subTest():
			correct = "5 added to Something"
			result = character_creator.add('Something', 5, test_dict)
			self.assertEqual(result, correct)
		with self.subTest():
			correct = "6 is more points than you have left in your pool"
			result = character_creator.add('Something', 6, test_dict)
			self.assertEqual(result, correct)
		with self.subTest():
			correct = "'this' is not a valid attribute"
			result = character_creator.add('this', 1, test_dict)
			self.assertEqual(result, correct)
	
	def test_4(self):
		self.maxDiff = None
		inputs = "2\nIntelligence\n10\n1\n0\n"
		correct = Tests.MENU
		correct += "What's your choice?\n"
		correct += "What attribute would you like to add points to?\n"
		correct += "How many points would you like to add?\n"
		correct += "10 added to Intelligence\n"
		correct += Tests.MENU
		correct += "What's your choice?\n"
		correct += '''
______________________________
Strength\t|\t0
Dexterity\t|\t0
Constitution\t|\t0
Wisdom\t\t|\t0
Intelligence\t|\t10
Charisma\t|\t0
Pool\t\t|\t62
______________________________\n'''
		correct += Tests.MENU
		correct += "What's your choice?\n"
		correct += "Goodbye.\n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)
		
	def test_5(self):
		test_dict = {'Something': 10,
					 'Pool': 0}
		with self.subTest():
			correct = "5 removed from Something"
			result = character_creator.remove('Something', 5, test_dict)
			self.assertEqual(result, correct)
		with self.subTest():
			correct = "6 is more points than you have left in Something"
			result = character_creator.remove('Something', 6, test_dict)
			self.assertEqual(result, correct)
		with self.subTest():
			correct = "'this' is not a valid attribute"
			result = character_creator.remove('this', 1, test_dict)
			self.assertEqual(result, correct)
	
	def test_6(self):
		self.maxDiff = None
		inputs = "2\nWisdom\n15\n3\nWisdom\n5\n1\n0\n"
		correct = Tests.MENU
		correct += "What's your choice?\n"
		correct += "What attribute would you like to add points to?\n"
		correct += "How many points would you like to add?\n"
		correct += "15 added to Wisdom\n"
		correct += Tests.MENU
		correct += "What's your choice?\n"
		correct += "What attribute would you like to remove points from?\n"
		correct += "How many points would you like to remove?\n"
		correct += "5 removed from Wisdom\n"
		correct += Tests.MENU
		correct += "What's your choice?\n"
		correct += '''
______________________________
Strength\t|\t0
Dexterity\t|\t0
Constitution\t|\t0
Wisdom\t\t|\t10
Intelligence\t|\t0
Charisma\t|\t0
Pool\t\t|\t62
______________________________\n'''
		correct += Tests.MENU
		correct += "What's your choice?\n"
		correct += "Goodbye.\n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)
	
	def test_7(self):
		self.maxDiff = None
		inputs = "2\ncharisma\n1\n3\nstrength\n1\n0\n"
		correct = Tests.MENU
		correct += "What's your choice?\n"
		correct += "What attribute would you like to add points to?\n"
		correct += "How many points would you like to add?\n"
		correct += "1 added to Charisma\n"
		correct += Tests.MENU
		correct += "What's your choice?\n"
		correct += "What attribute would you like to remove points from?\n"
		correct += "How many points would you like to remove?\n"
		correct += "1 is more points than you have left in Strength\n"
		correct += Tests.MENU
		correct += "What's your choice?\n"
		correct += "Goodbye.\n"
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
