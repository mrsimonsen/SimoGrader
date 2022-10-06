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

	inputs = "IDK\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_IDK(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "I don't know\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "IMHO\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_IMHO(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "in my humble opinion\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "JK\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test05_JK(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "just kidding\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "LOL\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test06_LOL(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "laughing out loud\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "TMI\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test07_TMI(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "too much information\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "ABC\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test08_Unknown(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "Unknown\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "bff\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test09_bff(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "best friend forever\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "idk\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test10_idk(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "I don't know\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "imho\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test11_imho(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "in my humble opinion\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "jk\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test12_jk(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "just kidding\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "lol\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test13_lol(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "laughing out loud\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "tmi\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test14_tmi(self, stdout):
		correct = "Input an abbreviation:\n"
		correct += "too much information\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

if __name__ == "__main__":
	unittest.main(module='tests', failfast=True)