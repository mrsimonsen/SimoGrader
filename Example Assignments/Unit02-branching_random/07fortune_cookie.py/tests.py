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


if __name__ == "__main__":
	unittest.main(module='tests', failfast=True)