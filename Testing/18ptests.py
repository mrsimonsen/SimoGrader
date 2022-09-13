import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "Some input\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1(self, stdout):
		correct = "Enter a sentence or phrase:\nYou entered: Some input\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	def test02_part_2(self):
		input = "Some input"
		correct = 9
		try:
			result = student.num_letters(input)
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail('Message: num_letters() function is missing')
		except TypeError:
			self.fail('Message: num_letters() function has incorrect parameters')

	inputs = "May the force be with you!\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3(self, stdout):
		correct = "Enter a sentence or phrase:\nYou entered: May the force be with you!\nNumber of letters: 20\n"
		try:
			student.main()
			result = stdout.getvalue()[:len(correct)]
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail('Message: num_letters() function is missing')
		except TypeError:
			self.fail('Message: num_letters() function has incorrect parameters')

	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_4(self, stdout):
		input = " lots  \nof \tspa\tc\tes\n\n"
		correct = "String with no whitespace: lotsofspaces\n"
		try:
			student.output_without_whitespace(input)
			result = stdout.getvalue()
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail('Message: output_without_whitespace() function is missing')
		except TypeError:
			self.fail('Message: output_without_whitespace() function has incorrect parameters')

	inputs = "Do. Or do not. There is no try.\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test05_part_5(self, stdout):
		correct = "Enter a sentence or phrase:\nYou entered: Do. Or do not. There is no try.\nNumber of letters: 21\nString with no whitespace: Do.Ordonot.Thereisnotry.\n"
		try:
			student.main()
			result = stdout.getvalue()
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail('Message: output_without_whitespace() function is missing')
		except TypeError:
			self.fail('Message: output_without_whitespace() function has incorrect parameters')

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
