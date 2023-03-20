import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	def test01_part_1(self):
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
	def test02_part_2(self, stdout):
		correct = "Channel: 3\nVolume: 5\n"
		try:
			r = student.Remote()
		except AttributeError:
			self.fail("Message: Remote class has not been defined.")
		print(r)
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3(self, stdout):
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
	def test04_part_4(self, stdout):
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
	def test05_part_5(self, stdout):
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
	def test06_part_6(self, stdout):
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

	def test07_part_7(self):
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

	def test08_part_8(self):
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
	def test09_part_8(self, stdout):
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
	def test10_part_8(self, stdout):
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


if __name__ == "__main__":
	unittest.main(module='tests', failfast=True)