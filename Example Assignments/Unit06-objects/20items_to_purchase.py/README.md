# Instructions
Objective: Learn how to create objects with attributes, methods,  constructors, and string representations.

## Steps
1. You've been given the main() method for this assignment. Do not edit it.
2. Create the Item class with a constructor that sets default values for the following public attributes:
	attribute|value
	--|--
	name|"none"
	price|0
	quantity|0

3. Create a method called total that returns the total value of the item.
4. Create a string method that returns the attributes of the object like this example: ``Cookies 2 @ $0.76 = $1.52``. Format the price and total to always display to 2 rounded decimal places.
5. Display the total cost of all the items, rounded to 2 decimal places.

The output of the program should look like the following:
```
Item 1
Enter the item name:
Bottled Water
Enter the item price:
.96
Enter the item quantity:
5
Item 2
Enter the item name:
Cookies
Enter the item price:
2.5
Enter the item quantity:
3
TOTAL COST
Bottled Water 5 @ $0.96 = $4.80
Cookies 3 @ $2.50 = $7.50
Total: $12.30
```
*Note: This program outputs a newline after each input and the example show the user's input, but that actually isn't part of the output when the program runs.*