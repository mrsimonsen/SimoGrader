import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "5\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1(self, stdout):
		correct = "Input a side of a cube (in inches):\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "5\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_2(self, stdout):
		correct = "The cube's volume is 125 in^3.\n"
		student.main()
		result = stdout.getvalue()[36:len(correct)+36]
		self.assertEqual(result, correct)

	inputs = "5\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3(self, stdout):
		correct = "A sphere with the same volume has a diameter of 6.20 inches.\n"
		student.main()
		result = stdout.getvalue()[67:len(correct)+67]
		self.assertEqual(result, correct)

	inputs = "5\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_4(self, stdout):
		correct = "The cube would fit in a sphere with a diameter of 8.66 inches.\n"
		student.main()
		result = stdout.getvalue()[128:len(correct)+128]
		self.assertEqual(result, correct)

	inputs = "5\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test05_part_5(self, stdout):
		correct = "The weight of that volume in various metals:\nAluminum  = 12.25 lbs\nBronze-Al = 39.09 lbs\nCopper    = 40.50 lbs\nSilver    = 47.38 lbs\nRose Gold = 75.91 lbs\nGold      = 87.25 lbs\n"
		student.main()
		result = stdout.getvalue()[191:len(correct)+191]
		self.assertEqual(result, correct)

	inputs = "10\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test06_all(self, stdout):
		correct = '''Input a side of a cube (in inches):
The cube's volume is 1000 in^3.
A sphere with the same volume has a diameter of 12.41 inches.
The cube would fit in a sphere with a diameter of 17.32 inches.
The weight of that volume in various metals:
Aluminum  = 98.00 lbs
Bronze-Al = 312.70 lbs
Copper    = 324.00 lbs
Silver    = 379.00 lbs
Rose Gold = 607.25 lbs
Gold      = 698.00 lbs
'''
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

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
	report = f"Passed: {passed}/{total}\nScore: {score}\n"
	if not simple:
		failed = []
		for i in result.failures:
			failed.append(f"Fail: {i[0].id()[15:]}")
		for i in result.errors:
			failed.append(f"Error: {i[0].id()[15:]}")
		report += "Failed:\n"
		for i in failed:
			print(f"	{i}")
	return score

if __name__ == '__main__':
	simple = bool(sys.argv[1])
	score = main(simple)
	with open('score.txt','w') as f:
		f.write(str(score))
