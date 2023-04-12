import unittest, sys, pickle
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	def test01_part_3(self):
		correct = [('none',0.0,1), ("tacos", 1.5, 3)]
		try:
			item1 = student.Items.Generic()
			item2 = student.Items.Generic("tacos", 1.5, 3)
			result = []
			for item in (item1, item2):
				thing = (item.name, item.price, item.quantity)
				result.append(thing)
			self.assertEqual(result, correct)
		except TypeError:
			self.fail("Message: Genric class constructor doesn't allow given values.")

	inputs = "somthing that is really long, like over 50 characters\nMilk\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_4(self, stdout):
		correct_val = "Milk"
		correct_out = "Item names must be between 1 and 50 characters\nEnter a name for the item:\nItem names must be between 1 and 50 characters\nEnter a name for the item:\n"
		temp = student.Items.Generic()
		temp.name = ''
		result_out = stdout.getvalue()
		try:
			result_val = temp._Generic__name
			self.assertEqual(result_val, correct_val)
		except AttributeError:
			self.fail("Message: name has not been given properties to make it private.")
		self.assertEqual(result_out, correct_out)

	inputs = "-1\n5.23\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_5(self, stdout):
		correct_out = "That wasn't a float.\nEnter item price:\nPrice can't be less than $0.00\nEnter item price:\n"
		correct_val = 5.23
		temp = student.Items.Generic()
		temp.price = 'two'
		result_out = stdout.getvalue()
		try:
			result_val = temp._Generic__price
			self.assertEqual(result_val, correct_val)
		except AttributeError:
			self.fail("Message: price has not been given properties to make it private.")
		self.assertEqual(result_out, correct_out)

	inputs = "0\n5\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_6(self, stdout):
		correct_out = "That wasn't an integer.\nEnter item quantity:\nQuantity can't be less than 1, remove item instead.\nEnter item quantity:\n"
		correct_val = 5
		temp = student.Items.Generic()
		temp.quantity = 'ten'
		result_out = stdout.getvalue()
		try:
			result_val = temp._Generic__quantity
			self.assertEqual(result_val, correct_val)
		except AttributeError:
			self.fail("Message: quantity has not been given properties to make it private.")
		self.assertEqual(result_out, correct_out)

	def test05_part_7(self):
		correct = [('none',0.0,1,'Today'), ("Beef",3.46,3,'Tomorrow?')]
		try:
			item1 = student.Items.Produce()
			item2 = student.Items.Produce("Beef",3.46,3, expire = 'Tomorrow?')
			result = []
			for item in (item1, item2):
				thing = (item.name, item.price, item.quantity, item.expire)
				result.append(thing)
			self.assertEqual(result, correct)
		except TypeError:
			self.fail("Message: Produce class constructor doesn't allow given values.")

	inputs = "Tomorrow\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test06_part_8(self, stdout):
		correct_out = "Expiration cannot be empty.\nEnter expiration date:\n"
		correct_val = "Tomorrow"
		temp = student.Items.Produce()
		temp.expire = ''
		result_out = stdout.getvalue()
		try:
			result_val = temp._Produce__expire
			self.assertEqual(result_val, correct_val)
		except AttributeError:
			self.fail("Message: expire has not been given properties to make it private.")
		self.assertEqual(result_out, correct_out)

	def test07_part_9(self):
		correct = ('Billy Bob', 'Some day', [])
		try:
			temp = student.ShoppingCart.ShoppingCart('Billy Bob', 'Some day')
			result = (temp._ShoppingCart__name, temp._ShoppingCart__date, temp._ShoppingCart__cartItems)
			self.assertEqual(result, correct)
		except TypeError:
			self.fail("Message: ShoppingCart class constructor doesn't allow given values.")

	def test08_part_10(self):
		correct = 5
		cart = student.ShoppingCart.ShoppingCart('','')
		for i in range(2,4):
			cart._ShoppingCart__cartItems.append(student.Items.Generic())
			cart._ShoppingCart__cartItems[i-2].quantity = i
		try:
			result = cart.num_items()
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: ShoppingCart doesn't have num_items() method.")

	def test09_part_11(self):
		correct = 4.68
		cart = student.ShoppingCart.ShoppingCart('','')
		for i in range(2,4):
			cart._ShoppingCart__cartItems.append(student.Items.Generic())
			cart._ShoppingCart__cartItems[i-2].quantity = i
			cart._ShoppingCart__cartItems[i-2].price = i*.36
		try:
			result = cart.total_cost()
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: ShoppingCart doesn't have num_items() method.")

	@patch('sys.stdout', new_callable = StringIO)
	def test10_part_12_empty(self, stdout):
		correct = "Luke's Shopping Cart - Life Day\nNumber of Items: 0\n\nSHOPPING CART IS EMPTY\n\nTotal: $0.00\n"
		temp = student.ShoppingCart.ShoppingCart('Luke', "Life Day")
		print(temp)
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	@patch('sys.stdout', new_callable = StringIO)
	def test11_part_12_full(self, stdout):
		correct = "Bob's Shopping Cart - Jan 1, 2020\nNumber of Items: 7\n\nCookies 2 @ $2.36 = $4.72, Expiration: Tomorrow\nnapkins 5 @ $0.45 = $2.25\n\nTotal: $6.97\n"
		cart = student.ShoppingCart.ShoppingCart("Bob", "Jan 1, 2020")
		cart._ShoppingCart__cartItems.append(student.Items.Produce('Cookies',2.36,2,expire = 'Tomorrow'))
		cart._ShoppingCart__cartItems.append(student.Items.Generic('napkins',.45,5))
		print(cart)
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs ='a\nProduce\nCookies\n2.36\n2\nTomorrow\ng\nnapkins\n.45\n5\n'
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test12_part_13(self,stdout):
		correct_val = [student.Items.Produce('Cookies', 2.36,2, expire = 'Tomorrow').__str__(), student.Items.Generic('napkins',.45,5).__str__()]
		correct_out = "What type of item: 'G'eneric or 'P'roduce?\nThat wasn't a valid option, try again.\nWhat type of item: 'G'eneric or 'P'roduce?\nEnter a name for the item:\nEnter item price:\nEnter item quantity:\nEnter expiration date:\nWhat type of item: 'G'eneric or 'P'roduce?\nEnter a name for the item:\nEnter item price:\nEnter item quantity:\n"
		cart = student.ShoppingCart.ShoppingCart('','')
		try:
			cart.add_item()
			cart.add_item()
			result_out = stdout.getvalue()
			result_val = []
			for i in cart._ShoppingCart__cartItems:
				result_val.append(i.__str__())
			self.assertEqual(result_out, correct_out)
			self.assertEqual(result_val, correct_val)
		except AttributeError:
			self.fail("Message: ShoppingCart doesn't have an add_item() method.")

	inputs = "bob\nCookies\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test13_part_14(self, stdout):
		correct_out = "What is the item's name that you want to remove?\nItem not found in cart. Nothing removed.\nWhat is the item's name that you want to remove?\n"
		correct_val = []
		cart = student.ShoppingCart.ShoppingCart('','')
		try:
			cart._ShoppingCart__cartItems.append(student.Items.Generic('Cookies'))
			cart.remove_item()
			cart.remove_item()
			result_out = stdout.getvalue()
			result_val = cart._ShoppingCart__cartItems
			self.assertEqual(result_out, correct_out)
			self.assertEqual(result_val, correct_val)
		except AttributeError:
			self.faild("Message: ShoppingCart doesn't have a remove_item() method.")

	inputs = "cups\n5\nCookies\n3\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test14_part_15(self, stdout):
		correct_out = "What item do you want to change?\nWhat's the new quantity?\nItem not found in cart. Nothing modified.\nWhat item do you want to change?\nWhat's the new quantity?\n"
		correct_val = [student.Items.Generic('napkins',.45,5).__str__() ,student.Items.Produce('Cookies', 2.36,3, expire = 'Tomorrow').__str__()]
		try:
			cart = student.ShoppingCart.ShoppingCart("",'')
			cart._ShoppingCart__cartItems.append(student.Items.Generic('napkins',.45,5))
			cart._ShoppingCart__cartItems.append(student.Items.Produce('Cookies', 2.36,1, expire = 'Tomorrow'))
			cart.change_item()
			cart.change_item()
			result_out = stdout.getvalue()
			result_val = []
			for i in cart._ShoppingCart__cartItems:
				result_val.append(i.__str__())
			self.assertEqual(result_out, correct_out)
			self.assertEqual(result_val, correct_val)
		except AttributeError:
			self.fail("Message: ShoppingCart doens't have a change_item() method.")

	inputs = "Bob\nJan 1, 2020\na\nCookies\np\nCookies\n2.36\n2\n\nTomorrow\na\ng\n\npaper cups\nseven\n-20\n.76\ntwenty\n0\n20\nc\npaper cups\n10\nc\nnapkins\n5\na\ng\nThis is a really long item name, why would you type this out?\nnapkins\n.45\n5\nr\ncups\nr\npaper cups\no\nq\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test15_all(self, stdout):
		self.maxDiff = None
		correct = "Enter customer's name:\nEnter today's date:\n\n		MENU\n	a - Add item to cart\n	r - Remove item from cart\n	c - Change item quantity\n	o - Output shopping cart\n	q - Quit\n\nChoose an option:\nWhat type of item: 'G'eneric or 'P'roduce?\nThat wasn't a valid option, try again.\nWhat type of item: 'G'eneric or 'P'roduce?\nEnter a name for the item:\nEnter item price:\nEnter item quantity:\nEnter expiration date:\nExpiration cannot be empty.\nEnter expiration date:\n\n		MENU\n	a - Add item to cart\n	r - Remove item from cart\n	c - Change item quantity\n	o - Output shopping cart\n	q - Quit\n\nChoose an option:\nWhat type of item: 'G'eneric or 'P'roduce?\nEnter a name for the item:\nItem names must be between 1 and 50 characters\nEnter a name for the item:\nEnter item price:\nThat wasn't a float.\nEnter item price:\nPrice can't be less than $0.00\nEnter item price:\nEnter item quantity:\nThat wasn't an integer.\nEnter item quantity:\nQuantity can't be less than 1, remove item instead.\nEnter item quantity:\n\n		MENU\n	a - Add item to cart\n	r - Remove item from cart\n	c - Change item quantity\n	o - Output shopping cart\n	q - Quit\n\nChoose an option:\nWhat item do you want to change?\nWhat's the new quantity?\n\n		MENU\n	a - Add item to cart\n	r - Remove item from cart\n	c - Change item quantity\n	o - Output shopping cart\n	q - Quit\n\nChoose an option:\nWhat item do you want to change?\nWhat's the new quantity?\nItem not found in cart. Nothing modified.\n\n		MENU\n	a - Add item to cart\n	r - Remove item from cart\n	c - Change item quantity\n	o - Output shopping cart\n	q - Quit\n\nChoose an option:\nWhat type of item: 'G'eneric or 'P'roduce?\nEnter a name for the item:\nItem names must be between 1 and 50 characters\nEnter a name for the item:\nEnter item price:\nEnter item quantity:\n\n		MENU\n	a - Add item to cart\n	r - Remove item from cart\n	c - Change item quantity\n	o - Output shopping cart\n	q - Quit\n\nChoose an option:\nWhat is the item's name that you want to remove?\nItem not found in cart. Nothing removed.\n\n		MENU\n	a - Add item to cart\n	r - Remove item from cart\n	c - Change item quantity\n	o - Output shopping cart\n	q - Quit\n\nChoose an option:\nWhat is the item's name that you want to remove?\n\n		MENU\n	a - Add item to cart\n	r - Remove item from cart\n	c - Change item quantity\n	o - Output shopping cart\n	q - Quit\n\nChoose an option:\nBob's Shopping Cart - Jan 1, 2020\nNumber of Items: 7\n\nCookies 2 @ $2.36 = $4.72, Expiration: Tomorrow\nnapkins 5 @ $0.45 = $2.25\n\nTotal: $6.97\n\n		MENU\n	a - Add item to cart\n	r - Remove item from cart\n	c - Change item quantity\n	o - Output shopping cart\n	q - Quit\n\nChoose an option:\n"
		try:
			student.main()
			result = stdout.getvalue()
			self.assertEqual(result, correct)
		except NameError:
			print("Something wasn't imported correctly")
		except TypeError:
			print("Some class doesn't have a proper constructor")

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