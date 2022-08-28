import unittest, sys, subprocess
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	def test01_part_1(self):
		correct = "0011"
		result = student.convert(3)
		self.assertEqual(result, correct)

	def test02_part_1(self):
		correct = "1011 1101"
		result = student.convert(189)
		self.assertEqual(result, correct)

	def test03_part_2(self):
		correct = 'some text'
		subprocess.run(f'echo "{correct}" > test.txt', shell = True)
		student.write(correct)
		result = subprocess.run(['diff','binary.txt','test.txt'], capture_output = True, text = True)
		if result.stdout:
			self.fail("Message: text files were not the same.")
		elif result.stderr:
			self.fail("Message: 'binary.txt' doesn't exist")
		else:
			subprocess.run("rm test.txt binary.txt", shell = True)


if __name__ == "__main__":
	unittest.main(module='tests', failfast=True)