# Instructions
Objective: Lean how to use dictionaries.

## Steps
*You have been given the main() function for this program. Do not edit the main() function.*
1. Create the reset() function. It has no parameters and returns a new dictionary with the following values:

	Key|Value
	--|--
	Strength|0
	Dexterity|0
	Constitution|0
	Wisdom|0
	Intelligence|0
	Charisma|0
	Pool|[]

2. Create the table() function. This function take a dictionary as a parameter and returns a pretty view of the dictionary as a string. The top and bottom of the string are 30 underscore characters. Each attribute is left justified to 12 characters, and each value has a tab character before it. See the example output for the remainder of the formatting.

3. Create the randomize() function. This function takes no parameters and follows the sudocode below:
	```
	create an empty list
	append a random 6-sided dice roll to the list 4 times
	display "Rolled 4d6 " and the list
	remove the lowest value from the list
	display "Dropped " and whatever the lowest value was
	return the sum of the remaining 3 dice rolls
	```
4. Create the roll_pool() function. This function has a parameter of a dictionary and follow the sudocode below:
	```
	reset the given dictionary
	6 times
		get a random sum from randomize()
		append the sum to the dictionary's 'Pool'
	sort the dictionary's 'Pool' in ascending order
	return the new dictionary
	```
5. Create the add() function. This function takes in 3 parameters: an attribute name, an amount of points, and a dictionary. This function returns a string depending on the following sudocode:
	```
	if the attribute is in the dictionary and that attribute is not 'Pool'
		if the amount is in the 'Pool'
			remove that amount from the 'Pool'
			set the attribute in the dictionary to that amount
			return "{amount} assigned to {attribute}"
		if not then
			return "{amount} doesn't exist in your pool"
	otherwise
		return "'{attribute}' is not a valid attribute"
	```
6. Create the remove() function. This function take in 2 parameters: an attribute, and a dictionary. This function returns a string depending on the following sudocode:
	```
	if the attribute is in the dictionary and that attribute is not 'Pool'
		if the current attribute in the dictionary is greater than 0
			append the amount of the attribute in the dictionary to the 'Pool'
			sort the 'Pool'
			set the attribute to 0
			return "{attribute} reset and points sent back to pool"
		if not then
			return "{attribute} hasn't been assigned yet"
	otherwise
		return "'{attribute}' is not a valid attribute"
	```


The output of the program should look like the following:
```
DnD 5e Character Creator
	|Menu|
0 - Quit
1 - View Attributes Table
2 - Roll Pool
3 - Assign to Attribute
4 - Remove from Attribute
5 - Reset
What's your choice?
2
Rolled 4d6 [1, 1, 6, 2]
Dropped 1
Rolled 4d6 [4, 6, 6, 2]
Dropped 2
Rolled 4d6 [5, 6, 5, 2]
Dropped 2
Rolled 4d6 [4, 4, 6, 5]
Dropped 4
Rolled 4d6 [2, 1, 3, 4]
Dropped 1
Rolled 4d6 [1, 6, 1, 2]
Dropped 1
Attribute pool has been rolled.
	|Menu|
0 - Quit
1 - View Attributes Table
2 - Roll Pool
3 - Assign to Attribute
4 - Remove from Attribute
5 - Reset
What's your choice?
1
______________________________
Strength    |	0
Dexterity   |	0
Constitution|	0
Wisdom      |	0
Intelligence|	0
Charisma    |	0
Pool        |	[9, 9, 9, 15, 16, 16]
______________________________
	|Menu|
0 - Quit
1 - View Attributes Table
2 - Roll Pool
3 - Assign to Attribute
4 - Remove from Attribute
5 - Reset
What's your choice?
3
Assign a value to which attribute?
Wisdom
Which value do you wish to assign?
9
9 assigned to Wisdom
	|Menu|
0 - Quit
1 - View Attributes Table
2 - Roll Pool
3 - Assign to Attribute
4 - Remove from Attribute
5 - Reset
What's your choice?
4
Remove value from which attribute?
Wisdom
Wisdom reset and points sent back to pool
	|Menu|
0 - Quit
1 - View Attributes Table
2 - Roll Pool
3 - Assign to Attribute
4 - Remove from Attribute
5 - Reset
What's your choice?
5
All attributes have been reset.
	|Menu|
0 - Quit
1 - View Attributes Table
2 - Roll Pool
3 - Assign to Attribute
4 - Remove from Attribute
5 - Reset
What's your choice?
9
'9' is not a valid menu option.
	|Menu|
0 - Quit
1 - View Attributes Table
2 - Roll Pool
3 - Assign to Attribute
4 - Remove from Attribute
5 - Reset
What's your choice?
0
Goodbye.
```
*Note: This program outputs a newline after each input and the example show the user's input, but that actually isn't part of the output when the program runs. This program generates random numbers, your output will vary. I set the seed value for the tests so that the numbers will always be the same.*