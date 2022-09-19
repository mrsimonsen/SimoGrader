import shelve
#################################################
#Don't edit code above this line



#Don't modify code below this line
#################################################
def cart_menu(cart):
	choice = 'z'
	while choice != 's':
		print('''
		CART MENU
	a - Add item to cart
	r - Remove item from cart
	c - Change item quantity
	o - Output shopping cart
	s - Save cart and Quit to Main Menu
''')
		choice = 'z'
		while choice not in "arcos":
			choice = input("Choose an option:\n")
		if choice == 'a':
			cart.add_item()
		elif choice == 'r':
			cart.remove_item()
		elif choice == 'c':
			cart.change_item()
		elif choice == 'o':
			print(cart)
		elif choice == 's':
			save(cart)

def main():
	choice = 'z'
	while choice != 'q':
		print('''
		MAIN MENU
	l - Load an existing shopping cart
	n - Create a new shopping cart
	v - View all shopping carts
	q - Exit program
''')
		choice = 'z'
		while choice not in 'lnvq':
			choice = input("Choose an option:\n")
		if choice == 'l':
			cart = load()
			if cart:
				cart_menu(cart)
			else:
				print("No customer found with that name.")
		elif choice == 'n':
			cart_menu(new())
		elif choice == 'v':
			view()

class ShoppingCart():
	def __init__(self,name,date):
		self.__name = name
		self.__date = date
		self.__cartItems = []

	@property
	def name(self):
		return self.__name
	@property
	def date(self):
		return self.__date

	def __str__(self):
		rep = f"{self.__name}'s Shopping Cart - {self.__date}\n"
		rep += f"Number of Items: {self.num_items()}\n\n"
		if self.__cartItems:
			for item in self.__cartItems:
				rep+=item.__str__()+'\n'
		else:
			rep += "SHOPPING CART IS EMPTY\n"
		rep += f"\nTotal: ${self.total_cost():.2f}"
		return rep

	def total_cost(self):
		total = 0
		for item in self.__cartItems:
			total += (item.price * item.quantity)
		return total

	def num_items(self):
		total = 0
		for item in self.__cartItems:
			total += item.quantity
		return total

	def add_item(self):
		type = 'a'
		while type not in ('g','generic','p','produce','e','electronic'):
			type = input("What type of item: 'G'eneric, 'P'roduce, or 'E'lectronic?\n").lower()
			if 'g' in type:
				item = Generic()
			elif 'p' in type:
				item = Produce()
			elif 'e' in type:
				item = Electronic()
				type = 't'
			else:
				print("That wasn't a valid option, try again.")

		item.name = input("Enter a name for the item:\n")
		item.price = input("Enter item price:\n")
		item.quantity = input("Enter item quantity:\n")
		if 'p' in type:
			item.expire = input("Enter expiration date:\n")
		elif 't' in type:
			item.warranty = input("Does the customer want a warranty (Y/n)?\n")
		self.__cartItems.append(item)

	def remove_item(self):
		name = input("What is the item's name that you want to remove?\n")
		index = -1
		for i in range(len(self.__cartItems)):
			if self.__cartItems[i].name == name:
				index = i
		if index != -1:
			del self.__cartItems[index]
		else:
			print("Item not found in cart. Nothing removed.")

	def change_item(self):
		item = Generic()
		item.name = input("What item do you want to change?\n")
		item.quantity = input("What's the new quantity?\n")
		found = False
		for i in self.__cartItems:
			if i.name == item.name:
				i.quantity = item.quantity
				found = True

		if not found:
			print("Item not found in cart. Nothing modified.")

class Generic():
	def __init__(self, name = 'none', price = 0.0, quantity = 1):
		self.name = name
		self.price = price
		self.quantity = quantity

	def total(self):
		return self.quantity * self.price

	def __str__(self):
		return f"{self.name} {self.quantity} @ ${self.price:.2f} = ${self.total():.2f}"

	@property
	def name(self):
		return self.__name
	@name.setter
	def name(self, new):
		while len(new) not in range(1,51):
			print("Item names must be between 1 and 50 characters")
			new = input("Enter a name for the item:\n")
		self.__name = new

	@property
	def price(self):
		return self.__price
	@price.setter
	def price(self, new):
		valid = False
		while not valid:
			try:
				new = float(new)
			except ValueError:
				print("That wasn't a float.")
			else:
				if new < 0:
					print("Price can't be less than $0.00")
				else:
					self.__price = new
					valid = True
			if not valid:
				new = input("Enter item price:\n")

	@property
	def quantity(self):
		return self.__quantity
	@quantity.setter
	def quantity(self, new):
		valid = False
		while not valid:
			try:
				new = int(new)
			except ValueError:
				print("That wasn't an integer.")
			else:
				if new < 1:
					print("Quantity can't be less than 1, remove item instead.")
				else:
					self.__quantity = new
					valid = True
			if not valid:
				new = input("Enter item quantity:\n")

class Produce(Generic):
	def __init__(self, *args, expire = 'Today'):
		self.expire = expire
		super().__init__(*args)

	def __str__(self):
		rep = super().__str__()
		rep += f", Expiration: {self.expire}"
		return rep

	@property
	def expire(self):
		return self.__expire
	@expire.setter
	def expire(self, new):
		while new == "":
			print("Expiration cannot be empty.")
			new = input("Enter expiration date:\n")
		else:
			self.__expire = new

class Electronic(Generic):
	def __init__(self, *args, warranty = False):
		self.warranty = warranty
		super().__init__(*args)

	def __str__(self):
		rep = super().__str__()
		rep += f", Warranty = {self.warranty}"

	@property
	def warranty(self):
		return self.__warranty
	@warranty.setter
	def warranty(self, new):
		if new not in (True, False):
			if new.lower() in ('yes','y'):
				new = True
			else:
				new = False
		self.__warranty = new