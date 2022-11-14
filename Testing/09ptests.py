import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "May the force be with you!\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_2(self, stdout):
		correct = "Enter a message:\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "May the force be with you!\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_3_message(self, stdout):
		correct = 'Enter a message:\nThe first vowel is "a".\n'
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "aeiou"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3_a(self, stdout):
		correct = f'Enter a message:\nThe first vowel is "a".\n'
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)
	
	inputs = "eioua"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_3_e(self, stdout):
		correct = f'Enter a message:\nThe first vowel is "e".\n'
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "iouae"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test05_part_3_i(self, stdout):
		correct = f'Enter a message:\nThe first vowel is "i".\n'
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)


	inputs = "ouaei"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test06_part_3_o(self, stdout):
		correct = f'Enter a message:\nThe first vowel is "o".\n'
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "uaeio"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test07_part_3_u(self, stdout):
		correct = f'Enter a message:\nThe first vowel is "u".\n'
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