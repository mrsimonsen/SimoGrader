from subprocess import run
from os import getcwd
import sys

#03p
file = "coin_flipper.py"
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
	inputs = "2\n"
	correct = "How many times do you want to flip the coin?\n"
	result = catchOutput(inputs)[:len(correct)]
	if result == correct:
		passed += 1
	else:
		failed.append("test1")

def test2():
	global total, passed
	total += 1
	inputs = "10\n"
	correct = "How many times do you want to flip the coin?\n"
	correct += "The coin was flipped 10 times.\nHeads: 5\tTails: 5\n"
	result = catchOutput(inputs, '1')
	if result == correct:
		passed += 1
	else:
		failed.append("test2")

def test3():
	global total, passed
	total += 1
	inputs = "100\n"
	correct = "How many times do you want to flip the coin?\n"
	correct1 = correct + "The coin was flipped 100 times.\nHeads: 40\tTails: 60\n"
	correct2 = correct + "The coin was flipped 100 times.\nHeads: 60\tTails: 40\n"
	result = catchOutput(inputs, '9')
	if result == correct1 or result == correct2:
		passed += 1
	else:
		failed.append("test3")

def hidden1():
	global total, passed
	total += 1
	inputs = "10\n"
	correct = "How many times do you want to flip the coin?\n"
	correct1 = correct + "The coin was flipped 10 times.\nHeads: 3\tTails: 7\n"
	correct2 = correct + "The coin was flipped 10 times.\nHeads: 7\tTails: 3\n"
	result = catchOutput(inputs, '14')
	if result == correct1 or result == correct2:
		passed += 1
	else:
		failed.append("hidden1")

# setup methods
def catchOutput(inputs=None, seed=''):
	p = run(f"python3 {file} {seed}", capture_output=True, text=True, shell=True, input=inputs)
	return p.stdout

if __name__ == "__main__":
	main()
