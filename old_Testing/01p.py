from subprocess import run
from os import getcwd
import sys

#01p
file = "calculator.py"
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
	correct = "Enter a number:\nEnter a second number:\nDoing math for 1 and 2.\n"
	inputs = "1\n2\n"
	result = catchOutput(inputs)[:len(correct)]
	if result == correct:
		passed += 1
	else:
		failed.append("test1")

def test2():
	global total, passed
	total += 1
	correct = "Enter a number:\nEnter a second number:\nDoing math for 1 and 2.\n"
	correct += "\nAddition = 3\nSubtraction = -1\nMultiplication = 2\nExponent = 1\nDivision = 0.5\nFloor Division = 0\nModulus Division = 1\n"
	inputs = "1\n2\n"
	result = catchOutput(inputs)
	if result == correct:
		passed += 1
	else:
		failed.append("test2")

def test3():
	global total, passed
	total += 1
	correct = "Enter a number:\nEnter a second number:\nDoing math for 1 and 16.\n"
	correct+="\nAddition = 17\nSubtraction = -15\nMultiplication = 16\nExponent = 1\nDivision = 0.062\nFloor Division = 0\nModulus Division = 1\n"
	inputs = "1\n16\n"
	result = catchOutput(inputs)
	if result == correct:
		passed += 1
	else:
		failed.append("test3")

def hidden1():
	global total, passed
	total += 1
	inputs = "23\n16\n"
	correct = "Enter a number:\nEnter a second number:\nDoing math for 23 and 16.\n"
	correct+="\nAddition = 39\nSubtraction = 7\nMultiplication = 368\nExponent = 6132610415680998648961\nDivision = 1.438\nFloor Division = 1\nModulus Division = 7\n"
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
