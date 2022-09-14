import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "Some message IDK\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1(self, stdout):
		correct = "Enter text:\nYou entered: Some message IDK\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "IDK if I'll go. It's my BFF's birthday.\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_message_1(self, stdout):
		correct = "Enter text:\nYou entered: IDK if I'll go. It's my BFF's birthday.\n"
		correct += "\tBFF: best friend forever\n\tIDK: I don't know\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "Nice pic, TMI haha JK. TTYL\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_message_2(self, stdout):
		correct = "Enter text:\nYou entered: Nice pic, TMI haha JK. TTYL\n"
		correct += "\tJK: just kidding\n\tTMI: too much information\n\tTTYL: talk to you later\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "TMI BFF JK IDK TTYL\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_all_5(self, stdout):
		correct = "Enter text:\nYou entered: TMI BFF JK IDK TTYL\n"
		correct += "\tBFF: best friend forever\n\tIDK: I don't know\n\tJK: just kidding\n\tTMI: too much information\n\tTTYL: talk to you later\n"
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
	simple = bool(sys.argv[1])
	score = main(simple)
	with open('score.txt','w') as f:
		f.write(str(score))
