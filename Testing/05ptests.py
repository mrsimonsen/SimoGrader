import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "a\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1(self, stdout):
		correct = "Input an abbreviation:\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "BFF\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_BFF(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "best friend forever\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "bff\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_bff(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "best friend forever\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "IDK\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_IDK(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "I don't know\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "idk\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test05_idk(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "I don't know\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "IMHO\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test06_IMHO(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "in my humble opinion\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "imho\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test07_imho(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "in my humble opinion\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "JK\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test08_JK(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "just kidding\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "jk\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test09_jk(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "just kidding\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "LOL\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test10_LOL(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "laughing out loud\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "lol\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test11_lol(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "laughing out loud\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "TMI\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test12_TMI(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "too much information\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "tmi\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test13_tmi(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "too much information\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "ABC\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test14_Unknown(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "Unknown\n"
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