import unittest, sys, random
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1(self, stdout):
		correct = "You crack open your cookie and your fortune falls out:\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test02_num_0(self, stdout):
		correct = "You crack open your cookie and your fortune falls out:\n"
		correct += '\tYou will read this and say "Geez! I could come up with better fortunes than that!"\n\tThis cookie is never gonna give you up, never gonna let you down.\n'
		random.seed(2)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test03_num_1(self, stdout):
		correct = "You crack open your cookie and your fortune falls out:\n"
		correct += '\tYou will read this and say "Geez! I could come up with better fortunes than that!"\n\tThis cookie is never gonna give you up, never gonna let you down.\n'
		random.seed(14)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test04_num_2(self, stdout):
		correct = "You crack open your cookie and your fortune falls out:\n"
		correct += '\tCookie said: "You really crack me up."\n\tThis cookie is never gonna give you up, never gonna let you down.\n'
		random.seed(1)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test05_num_3(self, stdout):
		correct = "You crack open your cookie and your fortune falls out:\n"
		correct += '\tYou are not illiterate.\n'
		random.seed(3)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test06_num_4(self, stdout):
		correct = "You crack open your cookie and your fortune falls out:\n"
		correct += '\tYou are not illiterate.\n'
		random.seed(13)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test07_num_5(self, stdout):
		correct = "You crack open your cookie and your fortune falls out:\n"
		correct += '\tHelp! I\'m being held prisoner in a fortune cookie bakery!\n\tYou will read this and say "Geez! I could come up with better fortunes than that!"\n'
		random.seed(7)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test08_num_6(self, stdout):
		correct = "You crack open your cookie and your fortune falls out:\n"
		correct += '\tHelp! I\'m being held prisoner in a fortune cookie bakery!\n'
		random.seed(0)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test09_num_7(self, stdout):
		correct = "You crack open your cookie and your fortune falls out:\n"
		correct += '\tHelp! I\'m being held prisoner in a fortune cookie bakery!\n'
		random.seed(9)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test10_num_8(self, stdout):
		correct = "You crack open your cookie and your fortune falls out:\n"
		correct += '\tThis cookie is never gonna give you up, never gonna let you down.\n'
		random.seed(17)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test11_num_9(self, stdout):
		correct = "You crack open your cookie and your fortune falls out:\n"
		correct += '\tCookie said: "You really crack me up."\n\tThis cookie is never gonna give you up, never gonna let you down.\n'
		random.seed(5)
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
	simple = bool(sys.argv[1])
	score = main(simple)
	with open('score.txt','w') as f:
		f.write(str(score))
