import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "IDK how that happened. TMI.\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1(self, stdout):
		correct = "Enter text:\nYou entered: IDK how that happened. TMI.\n\nFound \"IDK\", replaced with \"I don't know\"\nFound \"TMI\", replaced with \"too much information\"\n\nExpanded: I don't know how that happened. too much information.\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "I'll fix it. JK, you know IDK how.\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_2(self, stdout):
		correct = "Enter text:\nYou entered: I'll fix it. JK, you know IDK how.\n\nFound \"IDK\", replaced with \"I don't know\"\nFound \"JK\", replaced with \"just kidding\"\n\nExpanded: I'll fix it. just kidding, you know I don't know how.\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "Your bff, my BFF, and her BFF are all there. TTYL\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3(self, stdout):
		correct = "Enter text:\nYou entered: Your bff, my BFF, and her BFF are all there. TTYL\n\nFound \"BFF\", replaced with \"best friend forever\"\nFound \"TTYL\", replaced with \"talk to you later\"\n\nExpanded: Your bff, my best friend forever, and her best friend forever are all there. talk to you later\n"
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
		print(report)
	return score

if __name__ == '__main__':
	score = main(sys.argv[1]=='True')
	with open('score.txt','w') as f:
		f.write(str(score))
