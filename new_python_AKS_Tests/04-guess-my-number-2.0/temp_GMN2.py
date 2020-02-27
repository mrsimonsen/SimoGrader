#leave this code or testing won't work
import random, sys
if len(sys.argv)-1:
	random.seed(int(sys.argv[1]))
#########################################################

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")

# set the initial values
the_number = random.randint(1, 100)
tries = 1
guess = int(input("Take a guess: "))

# guessing loop
while guess != the_number:
	if guess > the_number:
		print("Lower...")
	else:
		print("Higher...")

	guess = int(input("Take a guess: "))
	tries += 1

print("You guessed it!  The number was", the_number)
print("And it only took you", tries, "tries!")