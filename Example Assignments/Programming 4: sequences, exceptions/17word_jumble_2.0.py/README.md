# Instructions
Objective: Learn how to work with 2 dimensional tuples.

## Steps
1. Read and run the given program to understand how it works. Then modify the intro to match the example output.
2. Expand the program so that it displays 'Goodbye.' if the player quits the game.
3. Expand the "that's not it" message to include the hint instructions.
4. Modify the 'WORDS' variable so that it's a 2D tuple, where each element is a tuple of a word and it's hint. Expand the branching so that if the user enters a '?' the paired hint prints out. Use the hints from the table below:
	word | hint
	:--: | --
	answer|what you're looking for
	difficult|not easy
	easy|not hard
	jumble|the name of the game
	python|a slithery coding language

	*Note: If the words and hints are not in the order listed above, the tests will not pass.*
5. Expand the guess correctly message so that it displays the appropriate message whether the player used a hint or not.


The output of the program should look like the following:
```
		Welcome to Word Jumble!

	Unscramble the letters to make a word.
	Type '?' if you want a hint.
	(Press the enter key at the prompt to quit.)

The jumble is: thypon

Your guess: guess
Sorry, that's not it.
Type '?' if you want a hint.
Your guess:
?
a slithery coding language
Your guess:
python
That's it! You guessed it!
Try to not use a hint next time.
Thanks for playing.
```
```
That's it! You guess it!
Good job not using a hint!
Thanks for playing.
```
*Note: This program outputs a newline after each input and the example show the user's input, but that actually isn't part of the output when the program runs. This program generates random numbers, your output will vary. I set the seed value for the tests so that the numbers will always be the same.*
