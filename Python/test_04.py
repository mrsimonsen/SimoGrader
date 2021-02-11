from subprocess import run
from os import getcwd
file = "GMN2.py"

# setup methods
def catchOutput(inputs=None, seed=''):
	cwd = getcwd()
	p = run(f"python3 {file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs)
	return p.stdout

def main():
	total = 0
	score = 0
	total += 1
	#def test_1(self):
	inputs = "50\n1\n1\n1\n1\n1\n1\n"
	correct = "\tWelcome to 'Guess My Number 2.0'!\n\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\n"
	result = catchOutput(inputs,"0")[:len(correct)]
	if result == correct:
		score += 1

	total += 1
	#def test_2(self):
	inputs = "50\n1\n1\n1\n1\n1\n1\n"
	correct = "\tWelcome to 'Guess My Number 2.0'!\n\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\nTake guess number 1:\n"
	result = catchOutput(inputs,'0')[:len(correct)]
	if result == correct:
		score += 1

	total += 1
	#def test_3(self):
	inputs = "50\n"
	correct = "\tWelcome to 'Guess My Number 2.0'!\n\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\nTake guess number 1:\n"
	correct += "You guessed it! The number was 50.\nAnd it only took you 1 tries!\n"
	result = catchOutput(inputs, "0")
	if result == correct:
		score += 1
	
	total += 1
	#def test_4(self):
	inputs = "1\n1\n1\n1\n100\n1\n1\n"
	correct = "\tWelcome to 'Guess My Number 2.0'!\n\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\nTake guess number 1:\n"
	correct += "Higher...\nTake guess number 2:\n" 
	correct += "Higher...\nTake guess number 3:\n"
	correct += "Higher...\nTake guess number 4:\n"
	correct += "Higher...\nTake guess number 5:\n"
	correct += "Lower...\nTake guess number 6:\n"
	correct += "You ran out of tries! The number was 18.\n"
	result = catchOutput(inputs,'1')
	if result == correct:
		score += 1
		
	#hidden tests
	total += 1
	def test_4(self):
		inputs = "50\n75\n90\n95\n93\n"
		correct = "\tWelcome to 'Guess My Number 2.0'!\n\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\nTake guess number 1:\n"
		correct += "Higher...\nTake guess number 2:\n" 
		correct += "Higher...\nTake guess number 3:\n"
		correct += "Higher...\nTake guess number 4:\n"
		correct += "Lower...\nTake guess number 5:\n"
		correct += "You guessed it! The number was 93.\nAnd it only took you 5 tries!\n"
		result = catchOutput(inputs,'20')
	if result == correct:
		score += 1
	
	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())
