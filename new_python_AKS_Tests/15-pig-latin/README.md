# 15-pig-latin

For this assignment you'll be creating a Pig Latin translator which asks the user for a message in a text file then creates a new text file with the pig latin version of the given message.
Hints:<br>
* .index() method works on any sequence
* take a look at the string methods lesson
* .isalpha() returns true if the character is a letter

In case you had a sheltered childhood, here's how pig latin works:


*For words that begin with consonants, the initial consonants up to the first vowel is moved to the end of the word, and "ay" is added.*
* "happy" &rarr; "appyhay"
* "glove" &rarr; "oveglay"
* "school" &rarr; "oolschay"

*For words that begin with vowels, "way" is added at the end of the word.*
* "egg" &rarr; "eggway"
* "inbox" &rarr; "inboxway"
* "eight" &rarr; "eightway"

(1) Create a global variables called 'VOWELS' that is a string of all the vowels in lowercase with no spaces.


(2)Create a function called way\_end() that takes one parameter: a string word. The function should return the pig latin traslation of the word.

(3)Create a function called ay\_end() that takes two parameters: a string word and an integer index position of the first vowel in the word. The function should return the pig latin translaton of the word. 


(4) Complete the  translate() function  that takes one parameter: a string of the original message. This function should split the message into individual words and send those words to the appropriate functions for translation. If the first letter of a word is not a letter, do not sent it for translation. Return the new message in all lowercase.


(5) Complete the write() function that takes one paramater: a string message. Create or overwrite a file called 'pig.txt' and write the given message into it. *This test won't work until you finish the next part*


(6) Complete the read() function that takes one paramater: a string file name. Use a try/except statment that either returns the message from the given file as a string or prints "--Could not open file!--" and returns the string "1error".


(7) Expand both ay\_end() and way\_end() to check for common punctuation at the end of the given word and place it at the end of the new pig latin word. Create a new global variable called END that contains ".,!?".
<br>
Example:<br>
"happy!" &rarr; "appyhay!"


(8) Expand both ay\_end() and way\_end() again to check for new line characters, which should always appear at the end of a given word when translated.
