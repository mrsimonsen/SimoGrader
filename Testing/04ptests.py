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
		simple = bool(sys.argv[1])
	score = main(simple)
	with open('score.txt','w') as f:
		f.write(str(score))
