# 11-guess-your-number

For this program main() is already completed and should not be altered.


(1) Complete the ask() function so that it prompts the user, and keeps prompting until it gets expected input. Make the input ignore case. Return the validated input.
```
Am I 'high', 'low' or 'correct'?
yo
Am I 'high', 'low' or 'correct'?
High
```
(2) Complete the end() function so that it returns an additional message before "Goodbye" based of if the computer won or not.
* computer victory message
	* "I know I could beat you, and in {tries} too!"
* player victory message
	* "I ran out of tries! You bested me!"
	
	
(3) Complete the high\_low() function to follow the pseudocode:
```
if the computer still has tries left
	if the user input was 'high'
		set new high value
		increment tries
	else if user input was 'low'
		set new low value
		increment tries
	else
		change play to false
else
	set play to false
return low, high, tries, play
```