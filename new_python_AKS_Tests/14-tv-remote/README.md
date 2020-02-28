# 14-tv-remote

The main() function is complete for this function and should not be edited.


(1) Create a Remote class. Give the class a constructor that sets private arrtibutes channel and volume to 3 and 5, respectively. Create a special string method that allow you to print an obect and display the following:
```
Channel: 3
Volume: 5
```
(2) Create the 'volume\_up' method that increases the current volume by 1. Don't allow the volume to go higher than 10.


(3) Create the 'volume\_down' method that decreases the current volume by 1. Don't allow the volume to go lower than 0.


(4) Create the 'channel\_up' method that goes to the next channel. If the channel is 100, the next channel is 1.


(5) Create the 'channel\_down' method that goes to the previous channel. If the channel is 1, the previous channel is 100.


(6) Create the 'set\_channel' method that tries to convert the new value into an int and set the channel to that value. If there is a ValueError, catch the error and display a message like the following:
```
What channel?
a
Error: {caught error message}
Explanation: 'a' isn't a number
```
(7) Create a property and setter for channel. Use the setter to only allow the channel attribute to be changed if it's within the min and max values. If it's not display a message like the following:
```
'3000' is out of the channel range
```