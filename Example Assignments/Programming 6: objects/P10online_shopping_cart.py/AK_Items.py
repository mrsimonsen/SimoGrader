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
