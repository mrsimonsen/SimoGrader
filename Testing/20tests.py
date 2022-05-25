import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	def test01_part_2(self):
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

	def test02_part_3(self):
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
	def test03_part_4(self,stdout):
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
	def test04_part_5(self, stdout):
		correct = "Item 1\nEnter the item name:\nEnter the item price:\nEnter the item quantity:\n\nItem 2\nEnter the item name:\nEnter the item price:\nEnter the item quantity:\n\nTOTAL COST\nBottled Water 5 @ $0.96 = $4.80\nCookies 3 @ $2.50 = $7.50\n\nTotal: $12.30\n"
		try:
			student.main()
			result = stdout.getvalue()
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: this test requires all other tests to work")
