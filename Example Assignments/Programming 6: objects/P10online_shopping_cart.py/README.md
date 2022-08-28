# Instructions
Project 10: extends assignment 21 with a structure like 22.

## Steps
1. You've been given the main() function for this assignment in the student.py file. Don't edit the main() function. You will need to modify the top of the studnet.py file to import your ShoppingCart file after its created.
	____
	### Items.py
1. Create a file called Items.py, it will have 2 class definitions in it: a generic item in class Generic, and produce item based on the generic item in class Produce.
2. Copy the contents of assignment 21's Item class into the Generic item class. Modify the constructor so that it can have default values for the attributes or given values for name, price, and quantity. The values should follow this table:
	attribute|value
	--|--
	name| *given name* or 'none'
	price| *given price* or 0.0
	quantity| *given quantity* or 1

	The total() and string methods should not be changed.
3. Convert the name into a private attribute by setting properties for it. The setter should follow this pseudocode:
	```
	while the length of the new name isn't between 1 and 50
		print "Item names must be between 1 and 50 characters"
		prompt for the new name again with "Enter a name for the item:\n"
	set the name to new name
	```
4. Convert the price into a private attribute by setting properties for it. The setter should follow this pseudocode:
	```
	set valid to false
	while not valid
		try to convert the new price to a float
		catch ValueError and print "That wasn't a float."
		if the try was successful
			if new is less than 0
				display "Price can't be less than $0.00"
			else:
				set price to the new price
				set valid to true
		if not valid:
			prompt for a new price again with "Enter item price:\n"
	```
5. Convert the quantity into a private attribute by setting properties for it. The setter should follow this pseudocode:
	```
	set valid to false
	while not valid
		try to convert the new quantity to an integer
		catch ValueError and print "That wasn't an integer."
		if the try was successful
			if new is less than 1
				display "Quantity can't be less than 1, remove item instead."
			else:
				set price to the new price
				set valid to true
		if not valid:
			prompt for a new price again with "Enter item quantity:\n"
	```
6. Copy assignment 21's Produce class into Items.py. Modify the constructor so that in addition to taking Generic values or defaults, it can have an attribute expire with a default value of "Today" or take a given value by key word. You'll need to use ``*args`` to catch and send the values for the Generic attributes.
7. Convert the expire into a private attribute by setting properties for it. The setter should follow this pseudocode:
	```
	while the length of the new expire is empty
		print "Expiration cannot be empty"
		prompt for the new expire again with "Enter expiration date:\n"
	set the expire to new expire
	```
	____
	### ShoppingCart.py
1. Create a file called ShoppingCart.py, import your classes from the Items.py file, and create the ShoppingCart class inside it. The ShoppingCart should have a constructor that takes in a name and date and sets the following private attributes:

		attribute|value
		--|--
		name | *given name*
		date | *given date*
		cartItems | *empty list*
	Since these attributes will not have properties, they need to be defined as private in the constructor.
2. The ShoppingCart should have a num_items() method that returns the total number of items in the cart. *Note: the number of items is **not** equal to the length of the cart.*
3. The ShoppingCart should have a total_cost() method that returns the total cost of all the items in the cart.
4. The ShoppingCart should have a string method that follows this pseudocode:
	```
	set string to customer's name and date
	add to string number of items in cart
	if there are cart items:
		add to the string the output of each items string method
	otherwise:
		add to the string "SHOPPING CART IS EMPTY"
	add to the string the total cost of the cart, rounding to 2 decimal places
	```
	That should look like the following:
	```
	Bob's Shopping Cart - Jan 1, 2020
	Number of Items: 7

	Cookies 2 @ $2.36 = $4.72, Expiration: Tomorrow
	napkins 5 @ $0.45 = $2.25

	Total: $6.97
	```
5. The ShoppingCart should have an add_item() method that follows this pseudocode:
	```
	while the type is not in ('g', 'generic', 'p', 'produce')
		prompt for the type with "What type of item: 'G'eneric or 'P'roduce?\n", force the input to be lower case
		if the type is generic
			make a generic item
		else if the type is produce
			make a produce item
		otherwise
			display "That wasn't a valid option, try again."
	prompt and set the item name with "Enter a name for the item:\n"
	prompt and set the item price with "Enter item price:\n"
	prompt and set the item quantity with "Enter item quantity:\n"
	if the type is produce:
		prompt and set the item expire with "Enter expiration date:\n"
	add the item to cartItems
	```
6. The ShoppingCart should have a remove_item() method that follows this pseudocode:
	```
	prompt for the name of the item to remove
	for every index in the range of the cartItems
		if the item's name at the current index matches the name we're searching for
			set a temp variable to that index
	if our temp variable has a value:
		delete the cartItem at that location
	otherwise
		display "Item not found in cart. Nothing removed."
	```
7. The ShoppingCart should have a change_item() method that follows this pseudocode:
	```
	make a generic temp item
	get and set the temp item's name with the prompt "What item do you want to change?\n"
	get and set the temp item's quantity with the prompt "What's the new quantity?\n"
	for each item in cartItems
		if the temp item's name matches the current item's name
			set the current item's quantity to the temp item's quantity
			set a temp variable to true
	if the temp variable is not true
		display "Item not found in cart. Nothing modified."
	```

The output of the program should look like the following:
```
Enter customer's name:
Bob
Enter today's date:
Jan 1, 2020

		MENU
	a - Add item to cart
	r - Remove item from cart
	c - Change item quantity
	o - Output shopping cart
	q - Quit

Choose an option:
a
What type of item: 'G'eneric or 'P'roduce?
Cookies
That wasn't a valid option, try again.
What type of item: 'G'eneric or 'P'roduce?
p
Enter a name for the item:
Cookies
Enter item price:
2.36
Enter item quantity:
2
Enter expiration date:

Expiration can not be empty.
Enter expiration date:
Tomorrow

		MENU
	a - Add item to cart
	r - Remove item from cart
	c - Change item quantity
	o - Output shopping cart
	q - Quit

Choose an option:
a
What type of item: 'G'eneric or 'P'roduce?
g
Enter a name for the item:

Item names must be between 1 and 50 characters
Enter a name for the item:
paper cups
Enter item price:
seven
That wasn't a float.
Enter item price:
-20
Price can't be less than $0.00
Enter item price:
.76
Enter item quantity:
twenty
That wasn't an integer.
Enter item quantity:
0
Quantity can't be less than 1, remove item instead.
Enter item quantity:
20

		MENU
	a - Add item to cart
	r - Remove item from cart
	c - Change item quantity
	o - Output shopping cart
	q - Quit

Choose an option:
c
What item do you want to change?
paper cups
What's the new quantity?
10

		MENU
	a - Add item to cart
	r - Remove item from cart
	c - Change item quantity
	o - Output shopping cart
	q - Quit

Choose an option:
c
What item do you want to change?
napkins
What's the new quantity?
5
Item not found in cart. Nothing modified.

		MENU
	a - Add item to cart
	r - Remove item from cart
	c - Change item quantity
	o - Output shopping cart
	q - Quit

Choose an option:
a
What type of item: 'G'eneric or 'P'roduce?
g
Enter a name for the item:
This is a really long item name, why would you type this out?
Item names must be between 1 and 50 characters
Enter a name for the item:
napkins
Enter item price:
.45
Enter item quantity:
5

		MENU
	a - Add item to cart
	r - Remove item from cart
	c - Change item quantity
	o - Output shopping cart
	q - Quit

Choose an option:
r
What is the item's name that you want to remove?
cups
Item not found in cart. Nothing removed.

		MENU
	a - Add item to cart
	r - Remove item from cart
	c - Change item quantity
	o - Output shopping cart
	q - Quit

Choose an option:
r
What is the item's name that you want to remove?
paper cups

		MENU
	a - Add item to cart
	r - Remove item from cart
	c - Change item quantity
	o - Output shopping cart
	q - Quit

Choose an option:
o
Bob's Shopping Cart - Jan 1, 2020
Number of Items: 7

Cookies 2 @ $2.36 = $4.72, Expiration: Tomorrow
napkins 5 @ $0.45 = $2.25

Total: $6.97

		MENU
	a - Add item to cart
	r - Remove item from cart
	c - Change item quantity
	o - Output shopping cart
	q - Quit

Choose an option:
q
```
*Note: This program outputs a newline after each input and the example show the user's input, but that actually isn't part of the output when the program runs.*
