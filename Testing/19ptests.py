import unittest, sys, random
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	maxDiff = None
	def test01_part_2(self):
		correct = [('Strength', 0), ('Dexterity', 0), ('Constitution', 0), ('Wisdom', 0), ('Intelligence', 0), ('Charisma', 0), ('Pool', [])]
		correct.sort()
		try:
			result = student.reset()
			if type(result) != type({}):
				self.fail("Message: reset() must return a dictionary")
			result = list(result.items())
			result.sort()
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: reset() function is missing or or doesn't return correctly")
		except TypeError:
			self.fail('Message: reset() function has incorrect parameters')

	def test02_part_3(self):
		try:
			temp = student.reset()
			for i in temp:
				if str(temp[i]).isdigit():
					temp[i] += 5
				else:
					for j in range(3):
						temp[i].append(j*5)
		except:
			self.fail('This test cannot be completed until the reset() function is defined')
		correct = "______________________________\nStrength    |	5\nDexterity   |	5\nConstitution|	5\nWisdom      |	5\nIntelligence|	5\nCharisma    |	5\nPool        |	[0, 5, 10]\n______________________________"
		try:
			result = student.table(temp)
			if type(result) != type(correct):
				self.fail('Message: table() function must return a string')
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail('Message: table() function is missing')
		except TypeError:
			self.fail('Message: table() function has incorrect parameters')

	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_4(self, stdout):
		correct_out = "Rolled 4d6 [4, 4, 1, 3]\nDropped 1\n"
		correct_sum = 11
		try:
			random.seed(0)
			result_sum = student.randomize()
			result_out = stdout.getvalue()
			self.assertEqual(result_sum, correct_sum)
			self.assertEqual(result_out, correct_out)
		except AttributeError:
			self.fail('randomize() function is missing')
		except TypeError:
			self.fail('Message: randomize() function has incorrect parameters')

	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_5_(self, stdout):
		try:
			temp = student.reset()
			for i in temp:
				if str(temp[i]).isdigit():
					temp[i] += 5
				else:
					for j in range(3):
						temp[i].append(j*5)
		except:
			self.fail('This test cannot be completed until the reset() function is defined')
		correct = {'Charisma': 0, 'Constitution': 0, 'Dexterity': 0, 'Intelligence': 0, 'Pool': [11, 12, 12, 15, 15, 15], 'Strength': 0, 'Wisdom': 0}
		try:
			random.seed(3)
			result = student.roll_pool(temp)
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail('roll_pool() function is missing')
		except TypeError:
			self.fail('Message: roll_pool() function has incorrect parameters')

	def test05_part_6(self):
		try:
			temp = student.reset()
			for i in temp:
				if str(temp[i]).isdigit():
					temp[i] += 5
				else:
					for j in range(3):
						temp[i].append(j*5)
		except:
			self.fail('This test cannot be completed until the reset() function is defined')
		with self.subTest("not valid attribute"):
			correct = "'Greatness' is not a valid attribute"
			try:
				result = student.add('Greatness', 10, temp)
				self.assertEqual(result, correct)
			except AttributeError:
				self.fail('add() function is missing')
			except TypeError:
				self.fail('Message: add() function has incorrect parameters')
		with self.subTest("amount doesn't exist"):
			correct = "8 doesn't exist in your pool"
			try:
				result = student.add('Wisdom', 8, temp)
				self.assertEqual(result, correct)
			except AttributeError:
				self.fail('add() function is missing')
			except TypeError:
				self.fail('Message: add() function has incorrect parameters')
		with self.subTest("success message"):
			correct = "10 assigned to Strength"
			try:
				result = student.add('Strength', 10, temp)
				self.assertEqual(result, correct)
				self.assertEqual(temp['Strength'],10, "add() didn't actually set the attribute value")
				self.assertEqual(temp['Pool'],[0,5], "add() didn't remove value from the Pool")
			except AttributeError:
				self.fail('add() function is missing')
			except TypeError:
				self.fail('Message: add() function has incorrect parameters')

	def test06_part_7(self):
		try:
			temp = student.reset()
			for i in temp:
				if str(temp[i]).isdigit():
					temp[i] += 5
				else:
					for j in range(3):
						temp[i].append(j*5)
		except:
			self.fail('This test cannot be completed until the reset() function is defined')
		with self.subTest("not valid attribute"):
			correct = "'Something' is not a valid attribute"
			try:
				result = student.remove('Something', temp)
				self.assertEqual(result, correct)
			except AttributeError:
				self.fail('remove() function is missing')
			except TypeError:
				self.fail('Message: remove() function has incorrect parameters')
		with self.subTest("amount doesn't exist"):
			correct = "Dexterity hasn't been assigned yet"
			try:
				temp['Dexterity'] = 0
				result = student.remove('Dexterity', temp)
				self.assertEqual(result, correct)
			except AttributeError:
				self.fail('remove() function is missing')
			except TypeError:
				self.fail('Message: remove() function has incorrect parameters')
		with self.subTest("success message"):
			correct = "Constitution reset and points sent back to pool"
			try:
				result = student.remove('Constitution', temp)
				self.assertEqual(result, correct)
				self.assertEqual(temp['Constitution'],0,"remove() didn't reset attribute to 0")
				self.assertEqual(temp['Pool'],[0,5,5,10],"remove() didn't append value to Pool and/or didn't sort Pool")
			except AttributeError:
				self.fail('remove() function is missing')
			except TypeError:
				self.fail('Message: remove() function has incorrect parameters')

def main(simple):
	suite = unittest.defaultTestLoader
	runner = unittest.TextTestRunner(stream=StringIO(), descriptions=False)
	result = runner.run(suite.loadTestsFromTestCase(Tests))
	total = result.testsRun
	if result.wasSuccessful():
		score = 10
		passed = total
	else:
		passed = total - len(result.failures) - len(result.errors)
		score = round(passed/total*10,2)
	print(f"Passed: {passed}/{total}")
	print(f"Score: {score}")
	if not simple:
		failed = []
		for i in result.failures:
			failed.append(f"Fail: {i[0].id()[15:]}")
		for i in result.errors:
			failed.append(f"Error: {i[0].id()[15:]}")
		print("Failed:")
		for i in failed:
			print(f"	{i}")
	return score

if __name__ == '__main__':
	try:
		simple = bool(sys.argv[1])
	score = main(simple)
	with open('score.txt','w') as f:
		f.write(str(score))
