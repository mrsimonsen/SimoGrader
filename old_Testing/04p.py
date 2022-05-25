from subprocess import run
from os import getcwd
import sys

#04p
file = "GMN2.py"
passed = 0
total = 0
failed = []

def main():
	global score, total
	simple()
	try:
		verbose = sys.argv[1]!='simple'
	except:
		verbose = True
	if verbose:
		print(f"Passed {passed} out of {total} tests.")
		if len(failed) > 0:
			print("Failed:")
			for i in failed:
				print(f"\t* {i}")

def simple():
	global score, total
	test1()
	test2()
	test3()
	test4()
	hidden1()
	print(f"{passed}/{total}")

def test1():
	global total, passed
	total += 1
	inputs = "50\n1\n1\n1\n1\n1\n1\n"
	correct = "\tWelcome to 'Guess My Number 2.0'!\n\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\n"
	result = catchOutput(inputs,"0")[:len(correct)]
	if result == correct:
		passed += 1
	else:
		failed.append("test1")

def test2():
	global total, passed
	total += 1
	inputs = "50\n1\n1\n1\n1\n1\n1\n"
	correct = "\tWelcome to 'Guess My Number 2.0'!\n\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\nTake guess number 1:\n"
	result = catchOutput(inputs,'0')[:len(correct)]
	if result == correct:
		passed += 1
	else:
		failed.append("test2")

def test3():
	global total, passed
	total += 1
	inputs = "50\n"
	correct = "\tWelcome to 'Guess My Number 2.0'!\n\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\nTake guess number 1:\n"
	correct += "You guessed it! The number was 50.\nAnd it only took you 1 tries!\n"
	result = catchOutput(inputs, "0")
	if result == correct:
		passed += 1
	else:
		failed.append("test3")

def test4():
	global total, passed
	total += 1
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
		passed += 1
	else:
		failed.append("test4")

def hidden1():
	global total, passed
	total += 1
	inputs = "50\n75\n90\n95\n93\n"
	correct = "\tWelcome to 'Guess My Number 2.0'!\n\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\nTake guess number 1:\n"
	correct += "Higher...\nTake guess number 2:\n"
	correct += "Higher...\nTake guess number 3:\n"
	correct += "Higher...\nTake guess number 4:\n"
	correct += "Lower...\nTake guess number 5:\n"
	correct += "You guessed it! The number was 93.\nAnd it only took you 5 tries!\n"
	result = catchOutput(inputs,'20')
	if result == correct:
		passed += 1
	else:
		failed.append("hidden1")

# setup methods
def catchOutput(inputs=None, seed=''):
	p = run(f"python3 {file} {seed}", capture_output=True, text=True, shell=True, input=inputs)
	return p.stdout

if __name__ == "__main__":
	main()
