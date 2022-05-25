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
