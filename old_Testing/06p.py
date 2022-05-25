from subprocess import run
from os import getcwd
import sys

#06p
file = "counter.py"
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
	inputs = "1\n10\n2\n"
	correct = "What is the starting number?\nWhat is the ending number?\nHow much should I count by?\nCounting from 1 to 10 by 2:"
	result = catchOutput(inputs)[:len(correct)]
	if result == correct:
		passed += 1
	else:
		failed.append("test1")

def test2():
	global total, passed
	total += 1
	inputs = "1\n10\n2\n"
	correct = "What is the starting number?\nWhat is the ending number?\nHow much should I count by?\nCounting from 1 to 10 by 2:\n"
	correct += "1 3 5 7 9 \n"
	result = catchOutput(inputs)
	if result == correct:
		passed += 1
	else:
		failed.append("test2")

def test3():
	global total, passed
	total += 1
	inputs = "3\n1\n-1\n"
	correct = "What is the starting number?\nWhat is the ending number?\nHow much should I count by?\nCounting from 3 to 1 by -1:\n"
	correct += "3 2 1 \n"
	result = catchOutput(inputs)
	if result == correct:
		passed += 1
	else:
		failed.append("test3")

def hidden1():
	global total, passed
	total += 1
	inputs = "1\n10\n1\n"
	correct = "What is the starting number?\nWhat is the ending number?\nHow much should I count by?\nCounting from 1 to 10 by 1:\n"
	correct += "1 2 3 4 5 6 7 8 9 10 \n"
	result = catchOutput(inputs)
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
