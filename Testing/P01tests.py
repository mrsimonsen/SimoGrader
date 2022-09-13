import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "1\n1\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1(self, stdout):
		correct = "Enter wall height (feet):\nEnter wall width (feet):\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "12\n15.5\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_2(self, stdout):
		correct = "Wall area: 186.0 square feet\n"
		student.main()
		result = stdout.getvalue()[51:len(correct)+51]
		self.assertEqual(result, correct)

	inputs = "12\n15.5\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3(self, stdout):
		correct = "Paint needed: 0.5314285714285715 gallons\n"
		student.main()
		result = stdout.getvalue()[80:len(correct)+80]
		self.assertEqual(result, correct)

	inputs = "14\n25\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_4(self, stdout):
		correct = "Enter wall height (feet):\nEnter wall width (feet):\n"
		correct += "Wall area: 350.0 square feet\n"
		correct += "Paint needed: 1.0 gallons\n"
		correct += "Cans needed: 1 cans\n"
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
		simple = sys.argv[1]
	except IndexError:
		simple = False
	score = main(simple)
	with open('score.txt','w') as f:
		f.write(str(score))
