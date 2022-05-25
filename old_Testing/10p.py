from subprocess import run
from os import getcwd
import sys

#10p
file = "scrambler.py"
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
	inputs = "This is my message.\n"
	correct = "What is the message to scramble?\n"
	correct += "There are 4 words in the message.\n"
	result = catchOutput(inputs)[:len(correct)]
	if result == correct:
		passed += 1
	else:
		failed.append('test1')

def test2():
	global total, passed
	total += 1
	inputs = "This is my message. \n"
	correct = "What is the message to scramble?\n"
	correct += "There are 5 words in the message.\n"
	correct += "Here's the shuffled message:\n"
	correct += "my is This  message.\n"
	result = catchOutput(inputs, '0')
	if result == correct:
		passed += 1
	else:
		failed.append('test2')

def hidden1():
	global total, passed
	total += 1
	inputs = "Wacky  multi   space message.\n"
	correct = "What is the message to scramble?\n"
	correct += "There are 7 words in the message.\n"
	correct += "Here's the shuffled message:\n"
	correct += "message. multi   space  Wacky\n"
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
