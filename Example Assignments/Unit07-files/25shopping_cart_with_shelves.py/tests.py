import unittest, sys, os
from unittest.mock import patch
from io import StringIO
from shelve import *
import student

class Tests(unittest.TestCase):
	inputs = "Luke Skywalker\nLong time ago\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_2(self, stdout):
		correct_out = "Enter customer's name:\nEnter today's date:\n"
		correct_data = ("Luke Skywalker", "Long time ago", [])
		try:
			obj = student.new()
			result_out = stdout.getvalue()
			result_data = (obj.name, obj.date, obj._ShoppingCart__cartItems)
			self.assertEqual(result_out, correct_out)
			self.assertEqual(result_data, correct_data)
		except AttributeError:
			self.fail("Message: new() function is missing or doesn't return correctly")
		except TypeError:
			self.fail('Message: some() function has incorrect parameters')

	inputs = "Luke Skywalker\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_3_and_4(self, stdout):
		obj = student.ShoppingCart("Luke Skywalker", "Long time ago")
		item1 = student.Electronic("Robotic Hand", 200, 1, warranty = True)
		obj._ShoppingCart__cartItems.append(item1)
		correct = obj.__str__()
		if os.path.exists('carts.bin'):
			os.remove('carts.bin')
		try:
			student.save(obj)
			result = student.load().__str__()
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: save() or load() function is missing or doesn't return correctly")
		if os.path.exists('carts.bin'):
			os.remove('carts.bin')

	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_5(self, stdout):
		correct = "Luke Skywalker - Long time ago\n\tItems: 1 @ $200.00\nDarth Vader - Longer time ago\n\tItems: 3 @ $600.00\n"

		item1 = student.Electronic("Robotic Hand", 200, 1, warranty = True)
		item2 = student.Electronic("Robotic Leg", 200, 2, warranty = True)
		obj1 = student.ShoppingCart("Luke Skywalker", "Long time ago")
		obj2 = student.ShoppingCart("Darth Vader", "Longer time ago")
		obj1._ShoppingCart__cartItems.append(item1)
		obj2._ShoppingCart__cartItems.append(item1)
		obj2._ShoppingCart__cartItems.append(item2)

		if os.path.exists('carts.bin'):
			os.remove('carts.bin')
		try:
			student.save(obj1)
			student.save(obj2)
			student.view()
			result = stdout.getvalue()
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: view() function is missing or doesn't return correctly")
		if os.path.exists('carts.bin'):
			os.remove('carts.bin')


if __name__ == "__main__":
	unittest.main(module='tests', failfast=True)