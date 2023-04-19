# Instructions
Objective: Learn how to create binary files for storing complex data.

## Steps
1. This is program uses a modified version of P10online_shopping_cart.py, with the majority of the code provided. Don't modify the code that's given to you.
2. Create the new() function: it takes in no parameters, prompts for a customer name and date, and returns a new ShoppingCart object. Check the example output for formatting.
3. Create the save(cart) function: it takes in a ShoppingCart as a parameter and returns nothing. Follow this pseudocode:
	```
	create or open 'carts.bin'
	create an entry in carts.bin for the given ShoppingCart object, using it's name as the key
	save and close carts.bin
	```
4. Create the load() function: it has no parameters and returns a ShoppingCart object. Follow this pseudocode:
	```
	prompt "Enter customer's name:\n"
	load the data from carts.bin
	get and return the ShoppingCart object stored with the customers name
	if there is no object with that name, return None
	```
5. Create the view() function: it has no parameters and returns nothing. Follow this pseudocode:
	```
	for each key in carts.bin
		display "{name} - {date}\n\t{num_items} @ ${total_cost}"
	```
	Round the total cost to 2 decimal places. Check the example output for the exact style.

The output of the program should look like the following:
```
		MAIN MENU
	l - Load an existing shopping cart
	n - Create a new shopping cart
	v - View all shopping carts
	q - Exit program
Choose an option:
n
Enter customer's name:
Vader
Enter today's date:
Tuesday
		CART MENU
	a - Add item to cart
	r - Remove item from cart
	c - Change item quantity
	o - Output shopping cart
	s - Save cart and Quit to Main Menu
Choose an option:
s
		MAIN MENU
	l - Load an existing shopping cart
	n - Create a new shopping cart
	v - View all shopping carts
	q - Exit program
Choose an option:
l
Enter customer's name:
Luke
No customer found with that name.
		MAIN MENU
	l - Load an existing shopping cart
	n - Create a new shopping cart
	v - View all shopping carts
	q - Exit program
Choose an option:
v
Vader - Tuesday
	Items: 0 @ $0.00
		MAIN MENU
	l - Load an existing shopping cart
	n - Create a new shopping cart
	v - View all shopping carts
	q - Exit program
Choose an option:
q
```
*Note: This program outputs a newline after each input and the example show the user's input, but that actually isn't part of the output when the program runs.*