from subprocess import run
from os import getcwd
file = "character_creator.py"
import character_creator
MENU = '''
\t\t\t ____
\t\t\t|Menu|
\t\t0 - Quit
\t\t1 - View Attributes and Pool
\t\t2 - Add to Attribute
\t\t3 - Remove from Attribute\n'''

# setup methods
def catchOutput(inputs=None, seed=''):
	cwd = getcwd()
	p = run(f"python3 {file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs)
	return p.stdout

def main():
	total = 0
	score = 0
	total += 1
	
	#test_1(self):
	inputs = "a\n0\n"
	correct = MENU
	correct += "What's your choice?\n"
	correct += "'a' is not a valid menu option.\n"
	correct += MENU
	correct += "What's your choice?\n"
	correct += "Goodbye.\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1
	total += 1
	#def test_2(self):A
	inputs = "1\n0\n"
	correct = MENU
	correct += "What's your choice?\n"
	correct += '''
______________________________
Strength\t|\t0
Dexterity\t|\t0
Constitution\t|\t0
Wisdom\t\t|\t0
Intelligence\t|\t0
Charisma\t|\t0
Pool\t\t|\t72
______________________________\n'''
	correct += MENU
	correct += "What's your choice?\n"
	correct += "Goodbye.\n"
	result = catchOutput(inputs, '0')
	if result == correct:
		score += 1
	
	total += 1
	#test 2B
	test_dict = {
		'Strength':10,
		'Dexterity':10,
		'Constitution':10,
		'Wisdom':10,
		'Intelligence':10,
		'Charisma': 10,
		'Pool':2}
	correct = '''
______________________________
Strength\t|\t10
Dexterity\t|\t10
Constitution\t|\t10
Wisdom\t\t|\t10
Intelligence\t|\t10
Charisma\t|\t10
Pool\t\t|\t2
______________________________'''
	result = character_creator.table(test_dict)
	if result == correct:
		score += 1
	
	total += 1
		#def test_3(self):A
	test_dict = {'Something': 0,
				 'Pool': 10}

	correct = "5 added to Something"
	result = character_creator.add('Something', 5, test_dict)
	if result == correct:
		score += 1
	total += 1
	#with self.subTest():B
	correct = "6 is more points than you have left in your pool"
	result = character_creator.add('Something', 6, test_dict)
	if result == correct:
		score += 1
	total += 1
	#with self.subTest():C
	correct = "'this' is not a valid attribute"
	result = character_creator.add('this', 1, test_dict)
	if result == correct:
		score += 1

	total += 1
	#def test_4(self):
	inputs = "2\nIntelligence\n10\n1\n0\n"
	correct = MENU
	correct += "What's your choice?\n"
	correct += "What attribute would you like to add points to?\n"
	correct += "How many points would you like to add?\n"
	correct += "10 added to Intelligence\n"
	correct += MENU
	correct += "What's your choice?\n"
	correct += '''
______________________________
Strength\t|\t0
Dexterity\t|\t0
Constitution\t|\t0
Wisdom\t\t|\t0
Intelligence\t|\t10
Charisma\t|\t0
Pool\t\t|\t62
______________________________\n'''
	correct += MENU
	correct += "What's your choice?\n"
	correct += "Goodbye.\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1
		
	#def test_5(self):
	test_dict = {'Something': 10,
				 'Pool': 0}
	total += 1
	#with self.subTest():A
	correct = "5 removed from Something"
	result = character_creator.remove('Something', 5, test_dict)
	if result == correct:
		score += 1
	total += 1
	#with self.subTest():B
	correct = "6 is more points than you have left in Something"
	result = character_creator.remove('Something', 6, test_dict)
	if result == correct:
		score += 1
	total += 1
	#with self.subTest():C
	correct = "'this' is not a valid attribute"
	result = character_creator.remove('this', 1, test_dict)
	if result == correct:
		score += 1

	total += 1
	#def test_6(self):
	inputs = "2\nWisdom\n15\n3\nWisdom\n5\n1\n0\n"
	correct = MENU
	correct += "What's your choice?\n"
	correct += "What attribute would you like to add points to?\n"
	correct += "How many points would you like to add?\n"
	correct += "15 added to Wisdom\n"
	correct += MENU
	correct += "What's your choice?\n"
	correct += "What attribute would you like to remove points from?\n"
	correct += "How many points would you like to remove?\n"
	correct += "5 removed from Wisdom\n"
	correct += MENU
	correct += "What's your choice?\n"
	correct += '''
______________________________
Strength\t|\t0
Dexterity\t|\t0
Constitution\t|\t0
Wisdom\t\t|\t10
Intelligence\t|\t0
Charisma\t|\t0
Pool\t\t|\t62
______________________________\n'''
	correct += MENU
	correct += "What's your choice?\n"
	correct += "Goodbye.\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1

	total += 1
	#def test_7(self):
	inputs = "2\ncharisma\n1\n3\nstrength\n1\n0\n"
	correct = MENU
	correct += "What's your choice?\n"
	correct += "What attribute would you like to add points to?\n"
	correct += "How many points would you like to add?\n"
	correct += "1 added to Charisma\n"
	correct += MENU
	correct += "What's your choice?\n"
	correct += "What attribute would you like to remove points from?\n"
	correct += "How many points would you like to remove?\n"
	correct += "1 is more points than you have left in Strength\n"
	correct += MENU
	correct += "What's your choice?\n"
	correct += "Goodbye.\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1
	
	#hidden tests
	total += 4
	inputs = "2\nstrength\n15\n2\ndexterity\n14\n2\nconstitution\n13\n2\nwisdom\n12\n2\nintelligence\n10\n2\ncharisma\n8\n1\n3\nstrength\n14\n3\ndexterity\n13\n3\nconstitution\n12\n3\nwisdom\n11\n3\nintelligence\n9\n3\ncharisma\n7\n1\n0\n"
	correct = '''
			 ____
			|Menu|
		0 - Quit
		1 - View Attributes and Pool
		2 - Add to Attribute
		3 - Remove from Attribute
What's your choice?
What attribute would you like to add points to?
How many points would you like to add?
15 added to Strength

			 ____
			|Menu|
		0 - Quit
		1 - View Attributes and Pool
		2 - Add to Attribute
		3 - Remove from Attribute
What's your choice?
What attribute would you like to add points to?
How many points would you like to add?
14 added to Dexterity

			 ____
			|Menu|
		0 - Quit
		1 - View Attributes and Pool
		2 - Add to Attribute
		3 - Remove from Attribute
What's your choice?
What attribute would you like to add points to?
How many points would you like to add?
13 added to Constitution

			 ____
			|Menu|
		0 - Quit
		1 - View Attributes and Pool
		2 - Add to Attribute
		3 - Remove from Attribute
What's your choice?
What attribute would you like to add points to?
How many points would you like to add?
12 added to Wisdom

			 ____
			|Menu|
		0 - Quit
		1 - View Attributes and Pool
		2 - Add to Attribute
		3 - Remove from Attribute
What's your choice?
What attribute would you like to add points to?
How many points would you like to add?
10 added to Intelligence

			 ____
			|Menu|
		0 - Quit
		1 - View Attributes and Pool
		2 - Add to Attribute
		3 - Remove from Attribute
What's your choice?
What attribute would you like to add points to?
How many points would you like to add?
8 added to Charisma

			 ____
			|Menu|
		0 - Quit
		1 - View Attributes and Pool
		2 - Add to Attribute
		3 - Remove from Attribute
What's your choice?

______________________________
Strength	|	15
Dexterity	|	14
Constitution	|	13
Wisdom		|	12
Intelligence	|	10
Charisma	|	13
Pool		|	0
______________________________

			 ____
			|Menu|
		0 - Quit
		1 - View Attributes and Pool
		2 - Add to Attribute
		3 - Remove from Attribute
What's your choice?
What attribute would you like to remove points from?
How many points would you like to remove?
14 removed from Strength

			 ____
			|Menu|
		0 - Quit
		1 - View Attributes and Pool
		2 - Add to Attribute
		3 - Remove from Attribute
What's your choice?
What attribute would you like to remove points from?
How many points would you like to remove?
13 removed from Dexterity

			 ____
			|Menu|
		0 - Quit
		1 - View Attributes and Pool
		2 - Add to Attribute
		3 - Remove from Attribute
What's your choice?
What attribute would you like to remove points from?
How many points would you like to remove?
12 removed from Constitution

			 ____
			|Menu|
		0 - Quit
		1 - View Attributes and Pool
		2 - Add to Attribute
		3 - Remove from Attribute
What's your choice?
What attribute would you like to remove points from?
How many points would you like to remove?
11 removed from Wisdom

			 ____
			|Menu|
		0 - Quit
		1 - View Attributes and Pool
		2 - Add to Attribute
		3 - Remove from Attribute
What's your choice?
What attribute would you like to remove points from?
How many points would you like to remove?
9 removed from Intelligence

			 ____
			|Menu|
		0 - Quit
		1 - View Attributes and Pool
		2 - Add to Attribute
		3 - Remove from Attribute
What's your choice?
What attribute would you like to remove points from?
How many points would you like to remove?
7 removed from Charisma

			 ____
			|Menu|
		0 - Quit
		1 - View Attributes and Pool
		2 - Add to Attribute
		3 - Remove from Attribute
What's your choice?

______________________________
Strength	|	1
Dexterity	|	1
Constitution	|	1
Wisdom		|	1
Intelligence	|	1
Charisma	|	1
Pool		|	66
______________________________

			 ____
			|Menu|
		0 - Quit
		1 - View Attributes and Pool
		2 - Add to Attribute
		3 - Remove from Attribute
What's your choice?
Goodbye.
'''
	result = catchOutput(inputs)
	if result == correct:
		score += 4
	
	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())