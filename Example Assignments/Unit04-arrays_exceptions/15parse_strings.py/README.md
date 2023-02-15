# Instructions
Objective: Learn how to unpack variables, use the string strip() method, and how to handle exceptions.

## Steps
1. Prompt the user for a string that contains two strings separated by a comma. Examples of strings that can be accepted:
   - some, string
   - some , string
   - some,string
2. Split and unpack the input string into two variables, then display them.
3. Keep prompting and splitting until the input is 'q'.
4. Expand the program so that it strips all leading and trailing white space from the two parts.
5. If there aren't the exact amount of variable matching the elements in the list when unpacking a ValueError is raised. Catch this exception and display a custom error message for missing a comma or more than one comma.

The output of the program should look like the following:
```
Enter input string:
some, string
First word: some
Second word: string
Enter input string:
thisstring
Error: No comma in string.
Enter input string:
this,string,
Error: Too many commas in string.
Enter input string:
q
```
*Note: This program outputs a newline after each input and the example show the user's input, but that actually isn't part of the output when the program runs.*
	