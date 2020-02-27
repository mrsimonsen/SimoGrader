#Name
#Period

#leave this code or testing won't work
import random, sys
if len(sys.argv)-1:
	random.seed(int(sys.argv[1]))
#########################################################

def end(tries, user):
	return "Goodbye."

def high_low(low, high, guess, user, tries, play):
	return low, high, tries, False

def ask():
	return 'correct'
	
def main():
	print("I am a special mind-reading machine and will guess the number you're thinking of between 1 and 100 in 6 tries or less.")
	print("After each guess, tell me if I'm 'high', 'low', or 'correct'.")

	high = 100
	low = 1
	play = True
	tries = 1
	while play:
		guess = random.randint(low, high)
		print(f"For try {tries} I guess {guess}")
		user = ask()
		low, high, tries, play = high_low(low, high, guess, user, tries, play)
	print(end(tries, user))

if __name__ == "__main__":
	main()