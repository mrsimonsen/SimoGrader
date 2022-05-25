from subprocess import run
from os import getcwd
import sys

import CC2
from random import seed

#13p
file = "CC2.py"
passed = 0
total = 0
failed = []
MENU = '''
Critter Caretaker

0 - Quit
1 - Listen to your critter
2 - Feed your critter
3 - Play with your critter\n'''

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
	seed(1)
	c = CC2.Critter('Bob')
	result = (c.hunger, c.boredom)
	correct = (2,9)
	if result == correct:
		passed += 1
	else:
		failed.append('test1')

def test2():
	global total, passed
	total += 1
	seed(0)
	c = CC2.Critter('Sue')
	result = c.__str__()
	correct = "Critter Object\nName: Sue\nHunger: 6\nBoredom: 6\nMood: frustrated"
	if result == correct:
		passed += 1
	else:
		failed.append('test2')

def test3():
	global total, passed
	total += 1
	inputs = 'Bob\n2\n1\n3\n9\n14\n0\n'
	correct = "What do you want to name your critter?\n"
	correct += MENU + "Choice:\n"
	correct += "How much food do you want to feed your critter?\n"
	correct += "Brruppp. Thank you.\n"
	correct += MENU + "Choice:\n"
	correct += "How much fun do you and your critter have?\n"
	correct += "Wheee!\n"
	correct += MENU + "Choice:\n"
	correct += "Critter Object\nName: Bob\nHunger: 7\nBoredom: 1\nMood: okay\n"
	correct += MENU + "Choice:\n"
	correct += "Goodbye.\n"
	result = catchOutput(inputs, '0')
	if result == correct:
		passed += 1
	else:
		failed.append('test3')

def hidden1():
	global total, passed
	total += 1
	inputs = "Dog\n1\n2\n10\n3\n10\n14\n0\n"
	correct = '''What do you want to name your critter?

Critter Caretaker

0 - Quit
1 - Listen to your critter
2 - Feed your critter
3 - Play with your critter
Choice:
I'm Dog and I feel okay now.

Critter Caretaker

0 - Quit
1 - Listen to your critter
2 - Feed your critter
3 - Play with your critter
Choice:
How much food do you want to feed your critter?
Brruppp. Thank you.

Critter Caretaker

0 - Quit
1 - Listen to your critter
2 - Feed your critter
3 - Play with your critter
Choice:
How much fun do you and your critter have?
Wheee!

Critter Caretaker

0 - Quit
1 - Listen to your critter
2 - Feed your critter
3 - Play with your critter
Choice:
Critter Object
Name: Dog
Hunger: 2
Boredom: 1
Mood: happy

Critter Caretaker

0 - Quit
1 - Listen to your critter
2 - Feed your critter
3 - Play with your critter
Choice:
Goodbye.
'''
	result = catchOutput(inputs, 4)
	if result == correct:
		passed += 1
	else:
		failed.append('hidden1')

# setup methods
def catchOutput(inputs=None, seed=''):
	p = run(f"python3 {file} {seed}", capture_output=True, text=True, shell=True, input=inputs)
	return p.stdout

if __name__ == "__main__":
	main()
