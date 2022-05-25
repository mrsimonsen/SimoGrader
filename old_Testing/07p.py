from subprocess import run
from os import getcwd
import sys

#07p
file = "reverse_message.py"
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
	hidden1()
	print(f"{passed}/{total}")

def test1():
	global total, passed
	total += 1
	inputs = "This is my message."
	correct = "What is your message?\n\nYour message reversed is:\n"
	correct += ".egassem ym si sihT\n"
	result = catchOutput(inputs)
	if result == correct:
		passed += 1
	else:
		failed.append("test1")

def test2():
	global total, passed
	total += 1
	inputs = "With some   space   . "
	correct = "What is your message?\n\nYour message reversed is:\n"
	correct += " .   ecaps   emos htiW\n"
	result = catchOutput(inputs)
	if result == correct:
		passed += 1
	else:
		failed.append("test2")

def hidden1():
	global total, passed
	total += 1
	inputs = "	because	I	tab"
	correct = "What is your message?\n\nYour message reversed is:\n"
	correct += "bat	I	esuaceb	\n"
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
