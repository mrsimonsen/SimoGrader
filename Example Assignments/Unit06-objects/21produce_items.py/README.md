# Instructions
Objective: Learn about polymorphism and inheritance.

## Steps
1. Copy your code from assignment 20. Add a new class called Produce that inherits from Item.
2. Overwrite the constructor to add ``self.expire = 'Today'``, then use the super() function to call the parent constructor.
3. Overwrite the string method so that in addition to the parent's string method output, it also has the following:
``, Expires: {self.expire}"``

The output of the program should look like the following:
```
Item 1
Enter the item name:
Cup
Enter the item price:
.5
Enter the item quantity:
3
Item 2
Enter the item name:
Milk
Enter the item price:
1.37
Enter the item quantity:
2
Enter the expiration date:
Tuesday
TOTAL COST
Cup 3 @ $0.50 = $1.50
Milk 2 @ $1.37 = $2.74, Expires: Tuesday
Total: $4.24
```
*Note: This program outputs a newline after each input and the example show the user's input, but that actually isn't part of the output when the program runs.*