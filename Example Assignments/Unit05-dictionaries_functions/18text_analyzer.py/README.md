# Instructions
Objective: Learn how to create functions and have functions communicate with each other through parameters and return statements.

## Steps
1. Prompt the user and display what they entered. Check the example output for formatting and what to say.
2. Create a function called num_letters() that takes in the user's input and returns the numeric count of the number of letters in the message. I suggest using the string method isalpha() for checking if a character in the string is a letter.
3. Display the output of the num_letters() function in main() following the formatting from the example output.
4. Create a function called output_without_whitespace() that takes in the user's input and returns nothing. This method displays the user's input without any whitespaces characters. I suggest using the string method isspace() to check if a character in the string is a whitespace character. Format the printed message as shown in the example output.
5. Call the output_without_whitespace() function in main.

The output of the program should look like the following:
```
Enter a sentence or phrase:
May the force be with you!
You entered: May the force be with you!
Number of letters: 20
String with no whitespace: Maytheforcebewithyou!
```
*Note: This program outputs a newline after each input and the example show the user's input, but that actually isn't part of the output when the program runs. This program generates random numbers, your output will vary. I set the seed value for the tests so that the numbers will always be the same.*