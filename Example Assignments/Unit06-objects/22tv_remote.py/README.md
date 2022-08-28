# Instructions
Objective: Learn about private attributes, getters and setters.

## Steps
1. You've been given the main() method for this assignment. Do not edit it.
2. Create the Remote class with a constructor that sets default values for the following private attributes:
	attribute|value
	--|--
	channel|3
	volume|5
3. Create a string method that returns the attributes of the object like this example:
```
Channel: 3
Volume: 5
```
4. Create a public volume_up() method that increases the private volume attribute by 1. Have the max volume be 10.
5. Create a public volume_down() method that decreases the private volume attribute by 1. Have the min volume be 0.
6. Create a public channel_up method that increases the private channel attribute by 1. Have the channel loop with a max channel of 100. As in channel_up 100 = 1
7. Create a public channel_down method that decreases the private channel attribute by 1. Have the channel loop with a min channel of 1. As in channel_down 1 = 100.
8. Create a getter for the private channel attribute.
9. Create a setter for the private channel attribute. The setter follows this psuedocode:
```
try to convert the new value to an int
if that fails display "Error: {e}", where {e} is the caught error message, and "Explanation: '{new}' isn't a number", where {new} is the new value
check if the converted new value is within the channel range
if it is, set the private channel attribute to the new value
otherwise display "'{new}' is out of the channel range"
```

The output of the program should look like the following:
```
Channel: 3
Volume: 5

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:
vu

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:
vu

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:
set
What channel?
14

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:
v
Channel: 14
Volume: 7

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:
q
Goodbye.
```
*Note: This program outputs a newline after each input and the example show the user's input, but that actually isn't part of the output when the program runs.*
