def main():
	print("\tWelcome to Guess My Number!")
	print("\nI'm thinking of a number between 1 and 100.")
	print("Try to guess it in as few attempts as possible.")

	# set the initial values
	the_number = random.randint(1, 100)
	tries = 1
	guess = int(input("Take a guess:\n"))

	# guessing loop
	while guess != the_number:
		if guess > the_number:
			print("Lower...")
		else:
			print("Higher...")

		guess = int(input("Take a guess:\n"))
		tries += 1

	print(f"You guessed it!  The number was {the_number}.")
	print(f"And it only took you {tries} tries!")