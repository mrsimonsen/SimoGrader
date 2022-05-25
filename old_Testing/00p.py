from subprocess import run
from os import getcwd
import sys

#00p
file = "hello_world.py"
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
	print(f"{passed}/{total}")

def test1():
	global total, passed
	total += 1
	correct = "Hello World!\n"
	result = catchOutput()[:len(correct)]
	if result == correct:
		passed += 1
	else:
		failed.append("test1")

def test2():
	global total, passed
	total += 1
	correct = "Hello World!\nNUAMES\n"
	result = catchOutput()[:len(correct)]
	if result == correct:
		passed += 1
	else:
		failed.append("test2")

def test3():
	global total, passed
	total += 1
	correct = "Hello World!\nNUAMES\nCS 1030\n"
	result = catchOutput()
	if result == correct:
		passed += 1
	else:
		failed.append("test3")

# no hidden tests for assignment 00

# setup methods
def catchOutput(inputs=None, seed=''):
	p = run(f"python3 {file} {seed}", capture_output=True, text=True, shell=True, input=inputs)
	return p.stdout

if __name__ == "__main__":
	main()
