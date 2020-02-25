#Mr. Simonsen
#Period 14

import random, sys

if len(sys.argv)-1:
	random.seed(int(sys.argv[1]))

WORDS = ("answer", "difficult", "easy", "jumble", "python")
HINTS = ("what you're looking for", 'not easy', 'not hard', 'the name of the game', 'a slithery coding language')

i = random.randrange(len(WORDS))
correct = WORDS[i]
word = correct
hint = HINTS[i]

jumble = ""
while word:
	i = random.randrange(len(word))
	jumble += word[i]
	word = word[:i] + word[(i + 1):]

print("\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n(Press the enter key at the prompt to quit.)\n")
print(f"The jumble is: {jumble}\n")
guess = 'guess'
hint_used = False
while guess != correct and guess != "":
	guess = input("Your guess:\n")
	if guess == correct:
		print("That's it! You guessed it!")
		if hint_used:
			print("Try to not use a hint next time.")
		else:
			print("Good job not using a hint!")
		print("Thanks for playing.")
	elif guess == '?':
		print(hint)
		hint_used = True
	elif guess == "":
		print("Goodbye.")
	else:
		print("Sorry, that's not it.")
		print("Type '?' if you want a hint.")