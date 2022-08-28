import AK_Items as Items

class ShoppingCart():
	def __init__(self,name,date):
		self.__name = name
		self.__date = date
		self.__cartItems = []

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
		while type not in ('g','generic','p','produce'):
			type = input("What type of item: 'G'eneric or 'P'roduce?\n").lower()
			if 'g' in type:
				item = Items.Generic()
			elif 'p' in type:
				item = Items.Produce()
			else:
				print("That wasn't a valid option, try again.")

		item.name = input("Enter a name for the item:\n")
		item.price = input("Enter item price:\n")
		item.quantity = input("Enter item quantity:\n")
		if 'p' in type:
			item.expire = input("Enter expiration date:\n")
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
		item = Items.Generic()
		item.name = input("What item do you want to change?\n")
		item.quantity = input("What's the new quantity?\n")
		found = False
		for i in self.__cartItems:
			if i.name == item.name:
				i.quantity = item.quantity
				found = True

		if not found:
			print("Item not found in cart. Nothing modified.")
