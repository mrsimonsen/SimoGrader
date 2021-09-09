from subprocess import run
from os import getcwd
import sys

#02p
file = "fortune_cookie.py"
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
	test5()
	print(f"{passed}/{total}")

def test1():
	global total, passed
	total += 1
	correct = "You crack open your cookie and your fortune falls out:\n"
	correct1 = correct + "Help! I'm being held prisoner in a fortune cookie bakery!\n"
	correct2 = correct + "Help! I’m being held prisoner in a fortune cookie bakery!\n"
	result = catchOutput(seed = "2")
	if result == correct1 or result == correct2:
		passed += 1
	else:
		failed.append("test1")

def test2():
	global total, passed
	total += 1
	correct = "You crack open your cookie and your fortune falls out:\n"
	correct += "Cookie said: \"You really crack me up.\"\n"
	result = catchOutput(seed = "1")
	if result == correct:
		passed += 1
	else:
		failed.append("test2")

def test3():
	global total, passed
	total += 1
	correct = "You crack open your cookie and your fortune falls out:\n"
	correct += "You are not illiterate.\n"
	result = catchOutput(seed = "7")
	if result == correct:
		passed += 1
	else:
		failed.append("test3")

def test4():
	global total, passed
	total += 1
	correct = "You crack open your cookie and your fortune falls out:\n"
	correct += "You will read this and say \"Geez! I could come up with better fortunes than that!\"\n"
	result = catchOutput(seed = "0")
	if result == correct:
		passed += 1
	else:
		failed.append("test4")

def test5():
	global total, passed
	total += 1
	correct = "You crack open your cookie and your fortune falls out:\n"
	correct += "This cookie is never gonna give you up, never gonna let you down.\n"
	result = catchOutput(seed = "5")
	if result == correct:
		passed += 1
	else:
		failed.append(test5)

# no hidden tests for assignment 02

# setup methods
def catchOutput(inputs=None, seed=''):
	p = run(f"python3 {file} {seed}", capture_output=True, text=True, shell=True, input=inputs)
	return p.stdout

if __name__ == "__main__":
	main()
