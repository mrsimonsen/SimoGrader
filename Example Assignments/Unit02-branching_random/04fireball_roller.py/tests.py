import unittest, sys, random
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1(self, stdout):
		correct = "A bright streak flashes from your pointing finger to a point you choose within range then blossoms with a low roar into an explosion of flame.\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_2(self, stdout):
		correct = "4 4 1 3 5 4 4 3\n"
		random.seed(0)
		student.main()
		result = stdout.getvalue()[143:len(correct)+143]
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3(self, stdout):
		correct = "Total damage: 28\n"
		random.seed(0)
		student.main()
		result = stdout.getvalue()[159:len(correct)+159]
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test04_min(self, stdout):
		correct = '''A bright streak flashes from your pointing finger to a point you choose within range then blossoms with a low roar into an explosion of flame.
1 1 1 1 1 1 1 1
Total damage: 8
'''
		random.seed(230317)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test05_max(self, stdout):
		correct = '''A bright streak flashes from your pointing finger to a point you choose within range then blossoms with a low roar into an explosion of flame.
6 6 6 6 6 6 6 6
Total damage: 48
'''
		random.seed(460439)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)


if __name__ == "__main__":
	unittest.main(module='tests', failfast=True)