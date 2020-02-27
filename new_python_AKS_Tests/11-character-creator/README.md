# 11-character-creator

(1) Create a program that displays a menu and prompts for user input until the user quits. Have a clause to catch if the user didn't enter a valid menu option.
```
	 	 ____
		|Menu|
	0 - Quit
	1 - View Attributes and Pool
	2 - Add to Attribute
	3 - Remove from Attribute
What is your choice?
a
'a' is not a valad menu option.
What is your choice?
0
Goodbye.
```
*Note: remember that the formatting is correct only on GitHub.com*


(2) Create a dictionary called 'atts' that has the six Dungeons and Dragons attributes as keys with values of 0 and another key for the point pool that starts at 72 (see below). Expand the program to have a table() function that takes a dictionary and returns a string that displays the dictionary formatted like below. Call this function when the user selects the "View Attributes and Pool" menu option.
```
What is your choice?
1
______________________________
Strength	|	0
Dexterity	|	0
Constitution	|	0
Wisdom		|	0
Intelligence	|	0
Charisma	|	0
Pool		|	72
______________________________
```
(3) Create a function called add() that takes three parameters: an attribute, an amount, and a dictionay; and returns a string. The function should work like the following pseudocode:
```
If the attribute is in the dictionary
	if the ammount is less than or equal to the points in the pool
		subtract that amount form the pool
		add that amount to the attribute
		return a message {amount} added to {attribute}
	else return a message {amount} is more points than you have left in your pool
else return a message '{attribute}' is not a valid attribute
```
(4) Implement the "Add to Attribute" menu option. Prompt the user for an attribute name. Prompt the user for a number of points to allocate. Call the add() function with its three arguments and print the resulting message. See the tests for the correct wording.


(5) Create a function called remove() that takes three parameters: an attribute, adn amount, and a dictionary; and returns a string. The function should work like the following pseudocode:
```
if the attribute is in the dictionary:
	if the ammount is less than or equal to the points in the attribute
		subtract the amount from the attribute
		add the amount to the pool
		return the message {amount} removed from {attribute}"
	else return the message {amount} is more points than you have left in {attribute}
else return the message '{attribute}' is not a valid attribute
```
(6) Implement the "Remove from Attribute" menu option. Prompt the user for an attribute name. Prompt the user for a number of points to allocate. Call the remove() function with its three arguments and print the resulting message. See the tests for the correct wording.


(7) Extend the program to automatically correct for capilization errors in attribute inputs in the "Remove from Attribute" and "Add to Attribute" menu options. 
