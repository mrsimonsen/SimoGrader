# 15-pig-latin


Write a Pig Latin translator which asks the user for a message then displays the pig latin version of the message. In case you had a sheltered childhood, here's how pig latin works:

*For words that begin with consonants, the initial consonant of consonant cluster is moved to the end of the word, and "ay" is added.*
* "happy" &rarr; "appyhay"
* "glove" &rarr; "oveglay"
* "school" &rarr; "oolschay"

*For words that begin with vowles, "way" is added at the end of the word.*
* "egg" &rarr; "eggway"
* "inbox" &rarr; "inboxway"
* "eight" &rarr; "eightway"

Create separate functions for adding the endings to individual words. **'ay_end'** takes two parameters, the word to be translated and the index position (int) of the first vowel. The function returns the new translation. **'way_end'** takes one parameter, the word to be translate and returns the new translation.

Write a separate function for translation called **'translator'** that takes one parameter, the original message, and returns the translated message in *lowercase* with the *first letter capitalized*. The 'translator' should split the message into individual words and send those words to the appropriate function for translation.  

Finally, have both 'ay_end' and 'way_end' check for punctuation ".,!?" at the end of the given word and place it at the end of the new pig latin word, instead of it being in the middle.
<br>
Example:<br>
happy! &rarr; "appyhay!"

Hints:<br>
* .index() method works on any sequence
* take a look at the string methods lesson
