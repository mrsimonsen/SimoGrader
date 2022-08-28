import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1_default(self, stdout):
		correct = " +303\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_1_extra(self, stdout):
		correct = "  -14\n"
		student.main(num=-14)
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_2_default(self, stdout):
		correct = "0012.34000\n"
		student.main()
		result = stdout.getvalue()[6:len(correct)+6]
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_2_extra(self, stdout):
		correct = "0003.14160\n"
		student.main(flt=3.1415962)
		result = stdout.getvalue()[6:len(correct)+6]
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test05_part_3_default(self, stdout):
		correct = "Format    Forma    Format\n"
		student.main()
		result = stdout.getvalue()[17:len(correct)+17]
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test06_part_3_extra(self, stdout):
		correct = "Simonsen  Simon  Simonsen\n"
		student.main(str="Simonsen")
		result = stdout.getvalue()[17:len(correct)+17]
		self.assertEqual(result, correct)


if __name__ == "__main__":
	unittest.main(module='tests', failfast=True)