import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "This is my message\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1(self, stdout):
		correct = "What is your message?\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "This is my message\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_2(self, stdout):
		correct = "The first character of the message is: T\n"
		student.main()
		result = stdout.getvalue()[22:len(correct)+22]
		self.assertEqual(result, correct)

	inputs = "stuff\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3(self, stdout):
		correct = "The last character of the message is: f\n"
		student.main()
		result = stdout.getvalue()[63:len(correct)+63]
		self.assertEqual(result, correct)

	inputs = "May the force be with you\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_4(self, stdout):
		correct = "The middle character of the message is: e\n"
		student.main()
		result = stdout.getvalue()[103:len(correct)+103]
		self.assertEqual(result, correct)

	inputs = "This is my message\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test05_part_5(self, stdout):
		correct = "Every 3rd character of the message:\nTssyea\n"
		student.main()
		result = stdout.getvalue()[145:len(correct)+145]
		self.assertEqual(result, correct)

	inputs = "May the force be with you\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test06_part_6(self, stdout):
		correct = "What is your message?\nThe first character of the message is: M\nThe last character of the message is: u\nThe middle character of the message is: e\nEvery 3rd character of the message:\nM eoeei u\nThe message reversed:\nuoy htiw eb ecrof eht yaM\n"
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
