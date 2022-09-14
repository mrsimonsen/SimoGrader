import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	def test01_part_1(self):
		correct = ("none", 0, 0)
		try:
			item = student.Produce()
		except AttributeError:
			self.fail("Message: Produce class has not been defined.")
		try:
			result = (item.name, item.price, item.quantity)
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: Produce does not inherit from Item.")

	def test02_part_2(self):
		correct = 'Today'
		try:
			item = student.Produce()
		except AttributeError:
			self.fail("Message: Produce class has not been defined.")
		try:
			result = item.expire
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: Produce missing expire attribute.")

	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3(self, stdout):
		correct = f"Milk 2 @ $1.37 = $2.74, Expires: Tuesday\n"
		try:
			item = student.Produce()
		except AttributeError:
			self.fail("Message: Produce class has not been defined.")
		try:
			item.name = 'Milk'
			item.quantity = 2
			item.price = 1.37
			item.expire = 'Tuesday'
			print(item)
			result = stdout.getvalue()
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: Produce missing attributes.")

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
