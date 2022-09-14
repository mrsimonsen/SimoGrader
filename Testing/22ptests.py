import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	def test01_part_2(self):
		correct = (3,5)
		try:
			r = student.Remote()
		except AttributeError:
			self.fail("Message: Remote class has not been defined.")
		try:
			channel = r._Remote__channel
		except AttributeError:
			self.fail("Message: channel attribute is not private")
		try:
			volume = r._Remote__volume
		except AttributeError:
			self.fail("Message: volume attribute is not private")
		result = (channel, volume)
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_3(self, stdout):
		correct = "Channel: 3\nVolume: 5\n"
		try:
			r = student.Remote()
		except AttributeError:
			self.fail("Message: Remote class has not been defined.")
		print(r)
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_4(self, stdout):
		correct = "Channel: 3\nVolume: 10\n"
		try:
			r = student.Remote()
		except AttributeError:
			self.fail("Message: Remote class has not been defined.")
		try:
			for i in range(7):
				r.volume_up()
		except AttributeError:
			self.fail("Message: volume_up() method has not been defined")
		print(r)
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_5(self, stdout):
		correct = "Channel: 3\nVolume: 0\n"
		try:
			r = student.Remote()
		except AttributeError:
			self.fail("Message: Remote class has not been defined.")
		try:
			for i in range(7):
				r.volume_down()
		except AttributeError:
			self.fail("Message: volume_down() method has not been defined")
		print(r)
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test05_part_6(self, stdout):
		correct = "Channel: 1\nVolume: 5\n"
		try:
			r = student.Remote()
		except AttributeError:
			self.fail("Message: Remote class has not been defined.")
		try:
			for i in range(98):
				r.channel_up()
		except AttributeError:
			self.fail("Message: channel_up() method has not been defined")
		print(r)
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test06_part_7(self, stdout):
		correct = "Channel: 100\nVolume: 5\n"
		try:
			r = student.Remote()
		except AttributeError:
			self.fail("Message: Remote class has not been defined.")
		try:
			for i in range(3):
				r.channel_down()
		except AttributeError:
			self.fail("Message: channel_down() method has not been defined")
		print(r)
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	def test07_part_8(self):
		correct = 3
		try:
			r = student.Remote()
		except AttributeError:
			self.fail("Message: Remote class has not been defined.")
		try:
			result = r.channel
		except AttributeError:
			self.fail("Message: channel attribute does not have a getter method")
		self.assertEqual(result, correct)

	def test08_part_9(self):
		correct = 14
		try:
			r = student.Remote()
		except AttributeError:
			self.fail("Message: Remote class has not been defined.")
		try:
			r.channel = 14
			result = r.channel
		except AttributeError:
			self.fail("Message: channel attribute does not have a setter method")
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test09_part_9(self, stdout):
		correct = "Error: invalid literal for int() with base 10: 'test'\nExplanation: 'test' isn't a number\n"
		try:
			r = student.Remote()
		except AttributeError:
			self.fail("Message: Remote class has not been defined.")
		try:
			r.channel = 'test'
			result = stdout.getvalue()
		except AttributeError:
			self.fail("Message: channel attribute does not have a setter method")
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test10_part_9(self, stdout):
		correct = "'3000' is out of the channel range\n"
		try:
			r = student.Remote()
		except AttributeError:
			self.fail("Message: Remote class has not been defined.")
		try:
			r.channel = 3000
			result = stdout.getvalue()
		except AttributeError:
			self.fail("Message: channel attribute does not have a setter method")
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
	report = f"Passed: {passed}/{total}\nScore: {score}\n"
	if not simple:
		failed = []
		for i in result.failures:
			failed.append(f"Fail: {i[0].id()[15:]}")
		for i in result.errors:
			failed.append(f"Error: {i[0].id()[15:]}")
		report += "Failed:\n"
		for i in failed:
			print(f"	{i}")
	return score

if __name__ == '__main__':
	simple = bool(sys.argv[1])
	score = main(simple)
	with open('score.txt','w') as f:
		f.write(str(score))
