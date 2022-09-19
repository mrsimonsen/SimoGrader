# Instructions
Project 11
## Steps
1. You've been given the main function in the student.py file. Don't edit the student.py file. You'll create a Tools.py file where all your code will go. Tools.py has already been imported into student.py.
2. Create the ask_yn(question) method. This function takes in a questions as a string, and returns a Boolean True or False. Follow this pseudocode:
	```
	while response isn't one of the following: y, yes, n, no
		get the lowercase response, prompting with the question
	if y is in the response:
		return True
	otherwise return False
	```
3. Create the get_cipher() method. This method take in no parameters and returns an integer. Follow this pseudocode:
	```
	while the key is not between 1 and 25 inclusive
		get an integer input form the user, prompting "What is the cipher key?\n"
		if the input wasn't a number display "That wasn't a number."
		if the input was a number but out of range, display "Cipher key must be between 1 and 25 inclusive."
	return the key
	```
4. Create the open_file(name) method. This function takes in a string of a file name and return a string of the contents of that file. Follow this pseudocode:
	```
	try to open the given file in read mode and get it's contents
	if the file cannot be found, catch the error and display "Couldn't find \"{file}\"."
	return the contents of the file or None
	```
5. Create the write(message) method. This function takes in a string message and returns nothing. Follow this pseudocode:
	```
	prompt for the name of a file with "What do you want to call the output file?\n"
	if the the file name doesn't end in ".txt"
		add ".txt" to the file name
	open a file of that name in write mode
	write the message to the file
	```
6. Create the encrypt(message, key) method. This function takes in two parameters: a string message and an integer key, then returns a string encrypted message. Follow this pseudocode:
	```
	if the given key is < 0:
		add 26 to the key
	for each character in the message:
		convert the character to an integer
		if the number represents a lowercase letter:
			add the key to the number
			if the number is no longer in the range of lowercase letters:
				wrap the number back to a lowercase letter(-26)
		if the number represents an uppercase letter:
			add the key to the number
			if the number is no longer in the range of uppercase letters:
				wrap the number back to a uppercase letter(-26)
		convert the number back to a character and add it to the encrypted message
	return the encrypted message
	```
	You'll need to use the [ord()](https://docs.python.org/3/library/functions.html#ord), and [chr()](https://docs.python.org/3/library/functions.html#chr) built-in functions in this function. Also, you'll need to reference the ASCII Table to know character's numeric values.
7. Create the decrypt(message, key) method. This function takes in an encrypted string and an integer key and returns the result of encrypt with the given message and negative key.
8. Create the analysis(message) method. This function takes in a string message and returns nothing. Follow this pseudocode:
	```
	Create an list with 26 elements, each a 0
	for each character in the message in lowercase:
		if the numeric equivalent of that character is a lowercase number:
			add 1 to the list index of that number - 97 (lowercase 'a')
	for each entry in the list:
		display {character version of index}: {number of that character, 0-led width to 2} {that many *s}
	```

The output of the program should look like the following:
```
```
*Note:*