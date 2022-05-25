from subprocess import run
from os import getcwd
import sys

#05p
file = "dice_roller.py"
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
	hidden1()
	print(f"{passed}/{total}")

def test1():
	global total, passed
	total += 1
	inputs = "5\n10\n"
	correct = "How many dice would you like to roll?\nHow many sides do the dice have?\nRolling 5x d10.\n"
	result = catchOutput(inputs)[:len(correct)]
	if result == correct:
		passed += 1
	else:
		failed.append("test1")

def test2():
	global total, passed
	total += 1
	inputs = "3\n4\n"
	correct = "How many dice would you like to roll?\nHow many sides do the dice have?\nRolling 3x d4.\n"
	correct += "Roll 1: 4\nRoll 2: 4\nRoll 3: 1\n"
	result = catchOutput(inputs, '0')[:len(correct)]
	if result == correct:
		passed += 1
	else:
		failed.append("test2")

def test3():
	global total, passed
	total += 1
	inputs = "3\n4\n"
	correct = "How many dice would you like to roll?\nHow many sides do the dice have?\nRolling 3x d4.\n"
	correct += "Roll 1: 2\nRoll 2: 1\nRoll 3: 3\n"
	correct += "Total: 6\n"
	result = catchOutput(inputs, '1')
	if result == correct:
		passed += 1
	else:
		failed.append("test3")

def hidden1():
	global total, passed
	total += 1
	inputs = "5\n20\n"
	correct = "How many dice would you like to roll?\nHow many sides do the dice have?\nRolling 5x d20.\n"
	correct += "Roll 1: 4\nRoll 2: 20\nRoll 3: 17\nRoll 4: 8\nRoll 5: 9\n"
	correct += "Total: 58\n"
	result = catchOutput(inputs, '14')
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
