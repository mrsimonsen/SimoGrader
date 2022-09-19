# Instructions
Project 6

## Steps
1. Read and run the given program to understand how it works. Then modify the intro to match the example output.
2. Modify the guess prompt so that it displays the current guess number, check the format from the example.
3. Modify the the ending message so that it displays a winning message or failing message correctly. (hint, the winning message has 2 conditions)
4. Modify the program so that it actually limits the user to 6 tries.

The output of the program should look like the following:
```
	Welcome to Guess My Number 2.0!
I'm thinking of a number between 1 and 100.
You have 6 attempts to guess my number.
Take guess number 1:
50
Lower...
Take guess number 2:
10
Higher...
Take guess number 3:
14
You guessed it! The number was 14.
And it only took you 3 tries.
```
```
You ran out of tries! The number was 14.
```
*Note: This program outputs a newline after each input and the example show the user's input, but that actually isn't part of the output when the program runs. This program generates random numbers, your output will vary. I set the seed value for the tests so that the numbers will always be the same.*