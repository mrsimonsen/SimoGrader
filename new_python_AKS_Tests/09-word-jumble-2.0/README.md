# 09-word-jumble-2.0

(1) Expand the branching so that when the player enters an empty string (just presses enter) "Goodbye." is displayed.
```
The jumble is: optynh
Your guess:

Goodbye.
```
(2) Expand the "that's not it" message to include instructions on how to access a hint.
```
Your guess:
blah
Sorry, that's not it.
Type '?' if you want a hint.
```
(3) Expand the Word Jumble game so that each word is paired with a hint. Add branching to the main while loop so that if the user types in a '?' the hint prints out. Use the following word-hint pairs for the program:
* answer
	* what you're looking for
* difficult
	* not easy
* easy
	* not hard
* jumble
	* the name of the game
* python
	* a slithery coding language
```
The jumble is: optynh
Your guess:
?
a slithery coding language
```
(4 + 5) Expand the guess correctly message so that an additional message is displayed depending on if they used a hint or not.
```
The jumble is: optynh
Your guess:
python
That's it! You guessed it!
Good job not using a hint!
Thanks for playing.
```
```
The jumble is: optynh
Your guess:
?
a slithery coding language
Your guess:
python
That's it! You guessed it!
Try to not use a hint next time.
Thanks for playing.
