import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	def test01_part_1(self):
		correct = ("none", 0, 0)
		try:
			item = student.Item()
		except AttributeError:
			self.fail("Message: Item class has not been defined.")
		try:
			result = (item.name, item.price, item.quantity)
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: Item missing attributes.")

	def test02_part_2(self):
		correct = 1.25
		try:
			item = student.Item()
			item.name = "Red Solo Cup"
			item.price = .25
			item.quantity = 5
		except AttributeError:
			self.fail("Message: Item class has not been defined.")
		try:
			result = item.total()
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: Item missing total() method.")

	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3(self,stdout):
		correct = "Cookies 2 @ $0.76 = $1.52\n"
		try:
			item = student.Item()
			item.name = "Cookies"
			item.price = .76
			item.quantity = 2
		except AttributeError:
			self.fail("Message: Item class has not been defined.")
		try:
			print(item)
			result = stdout.getvalue()
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: Item missing total property.")

	inputs = "Bottled Water\n.96\n5\nCookies\n2.5\n3\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_4(self, stdout):
		correct = "Item 1\nEnter the item name:\nEnter the item price:\nEnter the item quantity:\n\nItem 2\nEnter the item name:\nEnter the item price:\nEnter the item quantity:\n\nTOTAL COST\nBottled Water 5 @ $0.96 = $4.80\nCookies 3 @ $2.50 = $7.50\n\nTotal: $12.30\n"
		try:
			student.main()
			result = stdout.getvalue()
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: this test requires all other tests to work")

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
	report = f"Passed: {passed}/{total}\nScore: {score}\n"
	if not simple:
		failed = []
		for i in result.failures:
			failed.append(f"Fail: {i[0].id()[15:]}")
		for i in result.errors:
			failed.append(f"Error: {i[0].id()[15:]}")
		report += "Failed:\n"
		for i in failed:
			report += f"\t{i}\n"
	return score, report

if __name__ == '__main__':
	score, report = main(sys.argv[1]=='True')
	with open('score.txt','w') as f:
		f.write(str(score))
		f.write('\n'+report)