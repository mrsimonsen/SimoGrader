

#Do not edit below this line
#################################################
def main():
	name = input("Enter customer's name:\n")
	date = input("Enter today's date:\n")
	cart = ShoppingCart(name, date)
	choice = 'z'
	while choice != 'q':
		print('''
		MENU
	a - Add item to cart
	r - Remove item from cart
	c - Change item quantity
	o - Output shopping cart
	q - Quit
''')
		choice = 'z'
		while choice not in "arcoq":
			choice = input("Choose an option:\n")
		if choice == 'a':
			cart.add_item()
		elif choice == 'r':
			cart.remove_item()
		elif choice == 'c':
			cart.change_item()
		elif choice == 'o':
			print(cart)
