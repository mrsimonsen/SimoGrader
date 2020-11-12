from subprocess import run
from os import getcwd
file = "CC2.py"
import CC2
from random import seed
MENU = '''
Critter Caretaker

0 - Quit
1 - Listen to your critter
2 - Feed your critter
3 - Play with your critter\n'''

# setup methods
def catchOutput(inputs=None, seed=''):
	cwd = getcwd()
	p = run(f"python3 {file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs)
	return p.stdout

def main():
	total = 0
	score = 0
	
	total += 1
	#def test_1(self):
	seed(1)
	c = CC2.Critter('Bob')
	result = (c.hunger, c.boredom)
	correct = (2,9)
	if result == correct:
		score += 1
	
	total += 1
	#def test_2(self):
	seed(0)
	c = CC2.Critter('Sue')
	result = c.__str__()
	correct = "Critter Object\nName: Sue\nHunger: 6\nBoredom: 6\nMood: frustrated"
	if result == correct:
		score += 1
	
	total += 1
	#def test_3(self):
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
	correct2 = "What do you want to name your critter?\n"
	correct2 += MENU + "Choice:\n"
	correct2 += "How much food do you want to feed your critter?\n"
	correct2 += "Brruppp. Thank you.\n"
	correct2 += MENU + "Choice:\n"
	correct2 += "How much fun do you and your cirtter have?\n"
	correct2 += "Wheee!\n"
	correct2 += MENU + "Choice:\n"
	correct2 += "Critter Object\nName: Bob\nHunger: 7\nBoredom: 1\nMood: okay\n"
	correct2 += MENU + "Choice:\n"
	correct2 += "Goodbye.\n"
	result = catchOutput(inputs, '0')
	if result == correct or result == correct2:
		score += 1
	
	#hidden tests
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
	correct2 = '''What do you want to name your critter?

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
How much fun do you and your cirtter have?
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
	if result == correct or result == correct2:
		score += 1
	
	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())
