# Instructions
Project 9: Expands assignment 18

## Steps
1. You've been given the main function for this assignment, don't edit it. This project expands upon the logic of assignment 18, so have that code handy.
2. Create the print_menu() function, which has a string parameter of the user's sample text and returns the user's choice. Check the formatting from the example output. This function should match the following pseudocode:
	```
	Display entered sample text, starting with a newline
	Display menu options, ending with a newline
	while the user's choice is not within range
		try
			prompt the user for a choice
		except if it's not a integer
			print "That wasn't a number."
	return the user's choice
	```
3. Create the replace_exclamation() function, which takes the user's sample text as a parameter and returns a new string that replaces all occurrences of "!" with ".".
4. Create the shorten_space() function, which takes the user's sample text as a parameter and returns a new string that replaces all occurrences of multiple spaces with a single space and removes all leading and trailing whitespace.
5. Create the num_non_ws() function, which takes the user's sample text as a parameter and returns an integer count of characters that were not a whitespaces. This is a combination of the num_letters() and output_without_whitespace() functions from assignment 18.
6. Create the num_words() function, which takes the user's sample text as a parameter and returns a integer count of the number of words in the user's sample text. The number of words is equal to the length of the list that split the string at all spaces, after making sure that there is only single spaces in the text.
7. Create the find_text() function, which has 2 parameters: the word or phrase to find, and the user's sample text; then returns an integer of the word/phrase in the user's sample text.

The output of the program should look like the following:
```
Enter sample text:
  This   is sample! text!

Sample text: "  This   is sample! text! "
MENU
1 - Replace all !'s
2 - Shorten spaces
3 - Number of non-whitespace characters
4 - Number of words
5 - Find text
0 - Quit

Choose an option:
1
Edited text:   This   is sample. text.

Sample text: "  This   is sample. text. "
MENU
1 - Replace all !'s
2 - Shorten spaces
3 - Number of non-whitespace characters
4 - Number of words
5 - Find text
0 - Quit

Choose an option:
2
Edited text: This is sample. text.

Sample text: "This is sample. text."
MENU
1 - Replace all !'s
2 - Shorten spaces
3 - Number of non-whitespace characters
4 - Number of words
5 - Find text
0 - Quit

Choose an option:
3
Number of non-whitespace characters: 18

Sample text: "This is sample. text."
MENU
1 - Replace all !'s
2 - Shorten spaces
3 - Number of non-whitespace characters
4 - Number of words
5 - Find text
0 - Quit

Choose an option:
4
Number of words: 4

Sample text: "This is sample. text."
MENU
1 - Replace all !'s
2 - Shorten spaces
3 - Number of non-whitespace characters
4 - Number of words
5 - Find text
0 - Quit

Choose an option:
5
Enter a word or phrase to be found:
is
"is " instances: 2

Sample text: "This is sample. text."
MENU
1 - Replace all !'s
2 - Shorten spaces
3 - Number of non-whitespace characters
4 - Number of words
5 - Find text
0 - Quit

Choose an option:
0
```
*Note: This program outputs a newline after each input and the example show the user's input, but that actually isn't part of the output when the program runs.*
