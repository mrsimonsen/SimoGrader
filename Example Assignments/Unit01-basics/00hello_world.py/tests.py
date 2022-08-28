import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1(self, stdout):
		correct = "Hello World!\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_2(self, stdout):
		correct = "Hello World!\nNUAMES\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3(self, stdout):
		correct = "Hello World!\nNUAMES\n\tCS\n".replace("\t","<tab>").replace(" ","_")
		student.main()
		result = stdout.getvalue().replace("\t","<tab>").replace(" ","_")
		self.assertEqual(result, correct,"Note: spaces have been replaced with \"_\" and tabs have been replaced with \"<tab>\"")


if __name__ == "__main__":
	unittest.main(module='tests', failfast=True)