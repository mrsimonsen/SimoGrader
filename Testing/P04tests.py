import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "4\n14\n2022\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1(self, stdout):
		correct = "Enter a date and I'll tell you what weekday it was/is/will be.\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "4\n14\n2022\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_2(self, stdout):
		correct = "Enter a month (1-12):\nEnter a day (1-31):\nEnter a year (YYYY):\n"
		student.main()
		result = stdout.getvalue()[63:len(correct)+63]
		self.assertEqual(result, correct)

	inputs = "7\n20\n1969\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_sun(self, stdout):
		correct = "Enter a date and I'll tell you what weekday it was/is/will be.\nEnter a month (1-12):\nEnter a day (1-31):\nEnter a year (YYYY):\n\nSunday\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "3\n1\n1999\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_mon(self, stdout):
		correct = "Enter a date and I'll tell you what weekday it was/is/will be.\nEnter a month (1-12):\nEnter a day (1-31):\nEnter a year (YYYY):\n\nMonday\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "3\n1\n1988\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test05_tues(self, stdout):
		correct = "Enter a date and I'll tell you what weekday it was/is/will be.\nEnter a month (1-12):\nEnter a day (1-31):\nEnter a year (YYYY):\n\nTuesday\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "5\n10\n1797\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test06_wed(self, stdout):
		correct = "Enter a date and I'll tell you what weekday it was/is/will be.\nEnter a month (1-12):\nEnter a day (1-31):\nEnter a year (YYYY):\n\nWednesday\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "7\n4\n1776\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test07_thurs(self, stdout):
		correct = "Enter a date and I'll tell you what weekday it was/is/will be.\nEnter a month (1-12):\nEnter a day (1-31):\nEnter a year (YYYY):\n\nThursday\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "4\n14\n2028\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test08_fri(self, stdout):
		correct = "Enter a date and I'll tell you what weekday it was/is/will be.\nEnter a month (1-12):\nEnter a day (1-31):\nEnter a year (YYYY):\n\nFriday\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "1\n1\n2000\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test09_sat(self, stdout):
		correct = "Enter a date and I'll tell you what weekday it was/is/will be.\nEnter a month (1-12):\nEnter a day (1-31):\nEnter a year (YYYY):\n\nSaturday\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

def main(verbose=False):
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
	if verbose:
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
	main(True)
