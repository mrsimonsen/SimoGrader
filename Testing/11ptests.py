import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "0\n50\n5\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_1(self, stdout):
		correct = "Enter starting number:\nEnter ending number:\nEnter step number:\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "1\n10\n1\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_2(self, stdout):
		correct = "Enter starting number:\nEnter ending number:\nEnter step number:\nCounting from 1 to 10 by 1:\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "10\n0\n-3\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3(self, stdout):
		correct = "Enter starting number:\nEnter ending number:\nEnter step number:\nCounting from 10 to 0 by -3:\n10 7 4 1 \n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "1\n10\n1\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_4_positive(self, stdout):
		correct = "Enter starting number:\nEnter ending number:\nEnter step number:\nCounting from 1 to 10 by 1:\n1 2 3 4 5 6 7 8 9 10 \n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "10\n1\n-1\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test05_part_4_negative(self, stdout):
		correct = "Enter starting number:\nEnter ending number:\nEnter step number:\nCounting from 10 to 1 by -1:\n10 9 8 7 6 5 4 3 2 1 \n"
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
			report += f"\t{i}\n"
	return score, report

if __name__ == '__main__':
	score, report = main(sys.argv[1]=='True')
	with open('score.txt','w') as f:
		f.write(str(score))
		f.write('\n'+report)