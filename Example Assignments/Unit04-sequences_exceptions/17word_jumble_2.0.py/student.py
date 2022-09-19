import random
def main():
	# create a sequence of words to choose from
	WORDS = ("python", "jumble", "easy", "difficult", "answer")
	# pick one word randomly from the sequence
	word = random.choice(WORDS)
	# create a variable to use later to see if the guess is correct
	correct = word

	# create a jumbled version of the word
	jumble =""
	while word:
		position = random.randrange(len(word))
		jumble += word[position]
		word = word[:position] + word[(position + 1):]

	# start the game
	print("\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n(Press the enter key at the prompt to quit.)\n")
	print(f"The jumble is: {jumble}\n")

	guess = 'guess'
	while guess != correct and guess != "":
		guess = input("Your guess:\n")
		if guess == correct:
			print("That's it! You guessed it!")
			print("Thanks for playing.")
		else:
			print("Sorry, that's not it.")