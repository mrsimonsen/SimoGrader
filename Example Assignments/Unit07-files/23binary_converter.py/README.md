# Instructions
Objective: Learn about writing to text files.

## Steps
*I've given you the main function for this program, no need to modify it.*
1. You'll need to complete the convert function.
	* The binary string should always be a multiple of 4 digits in length. Add 0s to  the front of the binary string until the total length is evenly divisible by 4.
	* Now that the binary string is a multiple of 4, there add a space character every 4 digits.
2. Create the content for the write() function (delete the ``pass`` code). It takes in the formatted binary tree and writes it to a new text file called 'binary.txt'. Add a new line character to the end of the string.

The output of the program should look like the following:
```
Enter a number:
18
0001 0010
```
*Note: This program outputs a newline after each input and the example show the user's input, but that actually isn't part of the output when the program runs.*