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

def main(verbose=False):
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
	if verbose:
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
	main(True)
