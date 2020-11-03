from subprocess import run, TimeoutExpired, Popen, PIPE
from os import getcwd
file = "GMN2.py"

# setup methods
def catchOutput(inputs=None, seed=''):
	cwd = getcwd()
	result = None
	p = Popen(f"python3 {file} {seed}",stdin=PIPE,stdout=PIPE,shell=True,cwd=cwd, text=True)
	try:
		out = p.communicate(input=inputs, timeout=3)
		result = out[0]
	except TimeoutExpired:
		result = ""
		p.kill()
		run("ps fjx > kill.txt ", shell=True)
		with open('kill.txt','r') as f:
			data = f.readlines()
		k = data[-1].split(" ")
		run(f"kill {k[5]}",shell=True)
	return result

def main():
	total = 0
	score = 0
	total += 1
	#def test_1(self):
	inputs = "1\n1\n1\n1\n1\n1\n1\n"
	correct = "\tWelcome to 'Guess My Number 2.0'!\n\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\n"
	result = catchOutput(inputs,"0")[:len(correct)]
	if result == correct:
		score += 1

	total += 1
	#def test_2(self):
	inputs = "1\n1\n1\n1\n1\n1\n1\n"
	correct = "\tWelcome to 'Guess My Number 2.0'!\n\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\nTake guess number 1:\n"
	result = catchOutput(inputs, )[:len(correct)]
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
