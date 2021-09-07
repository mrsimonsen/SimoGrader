from subprocess import run
from os import getcwd
import sys

import character_creator

#12p
file = "character_creator.py"
passed = 0
total = 0
failed = []
MENU = '''
\t\t\t ____
\t\t\t|Menu|
\t\t0 - Quit
\t\t1 - View Attributes and Pool
\t\t2 - Add to Attribute
\t\t3 - Remove from Attribute\n'''


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
	test6()
	test7()
	test8()
	test9()
	test10()
	test11()
	test12()
	test13()
	hidden1()
	print(f"{passed}/{total}")

def test1():
	global total, passed
	total += 1
	inputs = "a\n0\n"
	correct = MENU
	correct += "What's your choice?\n"
	correct += "'a' is not a valid menu option.\n"
	correct += MENU
	correct += "What's your choice?\n"
	correct += "Goodbye.\n"
	result = catchOutput(inputs)
	if result == correct:
		passed += 1
	else:
		failed.append('test1')

def test2():
	global total, passed
	total += 1
	inputs = "1\n0\n"
	correct = MENU
	correct += "What's your choice?\n"
	correct += f'''
______________________________
{"Strength":12}|\t0
{"Dexterity":12}|\t0
{"Constitution":12}|\t0
{"Wisdom":12}|\t0
{"Intelligence":12}|\t0
{"Charisma":12}|\t0
{"Pool":12}|\t72
______________________________\n'''
	correct += MENU
	correct += "What's your choice?\n"
	correct += "Goodbye.\n"
	result = catchOutput(inputs, '0')
	if result == correct:
		passed += 1
	else:
		failed.append('test2')

def test3():
	global total, passed
	total += 1
	test_dict = {
		'Strength':10,
		'Dexterity':10,
		'Constitution':10,
		'Wisdom':10,
		'Intelligence':10,
		'Charisma': 10,
		'Pool':2}
	correct = f'''
______________________________
{"Strength":12}|\t10
{"Dexterity":12}|\t10
{"Constitution":12}|\t10
{"Wisdom":12}|\t10
{"Intelligence":12}|\t10
{"Charisma":12}|\t10
{"Pool":12}|\t2
______________________________'''
	result = character_creator.table(test_dict)
	if result == correct:
		passed += 1
	else:
		failed.append('test4')

def test5():
	global total, passed
	total+= 1
	test_dict = {'Something': 0,
				 'Pool': 10}
	correct = "5 added to Something"
	result = character_creator.add('Something', 5, test_dict)
	if result == correct:
		passed += 1
	else:
		failed.append('test5')

def test6():
	global total, passed
	total += 1
	test_dict = {'Something': 0,
				 'Pool': 10}
	correct = "6 is more points than you have left in your pool"
	result = character_creator.add('Something', 6, test_dict)
	if result == correct:
		passed += 1
	else:
		failed.append('test6')

def test7():
	global total, passed
	total += 1
	test_dict = {'Something': 0,
				 'Pool': 10}
	correct = "'this' is not a valid attribute"
	result = character_creator.add('this', 1, test_dict)
	if result == correct:
		passed += 1
	else:
		failed.append('test7')

def test8():
	global total, passed
	total += 1
	inputs = "2\nIntelligence\n10\n1\n0\n"
	correct = MENU
	correct += "What's your choice?\n"
	correct += "What attribute would you like to add points to?\n"
	correct += "How many points would you like to add?\n"
	correct += "10 added to Intelligence\n"
	correct += MENU
	correct += "What's your choice?\n"
	correct += f'''
______________________________
{"Strength":12}|\t0
{"Dexterity":12}|\t0
{"Constitution":12}|\t0
{"Wisdom":12}|\t0
{"Intelligence":12}|\t10
{"Charisma":12}|\t0
{"Pool":12}|\t62
______________________________\n'''
	correct += MENU
	correct += "What's your choice?\n"
	correct += "Goodbye.\n"
	result = catchOutput(inputs)
	if result == correct:
		passed += 1
	else:
		failed.append('test8')

def test9():
	global total, passed
	test_dict = {'Something': 10,
				 'Pool': 0}
	total += 1
	correct = "5 removed from Something"
	result = character_creator.remove('Something', 5, test_dict)
	if result == correct:
		passed += 1
	else:
		failed.append('test9')

def test10():
	global total, passed
	total += 1
	test_dict = {'Something': 10,
				 'Pool': 0}
	correct = "6 is more points than you have left in Something"
	result = character_creator.remove('Something', 6, test_dict)
	if result == correct:
		passed += 1
	else:
		failed.append('test10')

def test11():
	global total, passed
	total += 1
	test_dict = {'Something': 10,
				 'Pool': 0}
	correct = "'this' is not a valid attribute"
	result = character_creator.remove('this', 1, test_dict)
	if result == correct:
		passed += 1
	else:
		failed.append('test11')

def test12():
	global total, passed
	total += 1
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
	correct += f'''
______________________________
{"Strength":12}|\t0
{"Dexterity":12}|\t0
{"Constitution":12}|\t0
{"Wisdom":12}|\t10
{"Intelligence":12}|\t0
{"Charisma":12}|\t0
{"Pool":12}|\t62
______________________________\n'''
	correct += MENU
	correct += "What's your choice?\n"
	correct += "Goodbye.\n"
	result = catchOutput(inputs)
	if result == correct:
		passed += 1
	else:
		failed.append('test12')

def test13():
	global total, passed
	total += 1
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
		passed += 1
	else:
		failed.append('test13')

def hidden1():
	global total, passed
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
Strength    |	15
Dexterity   |	14
Constitution|	13
Wisdom      |	12
Intelligence|	10
Charisma    |	8
Pool        |	0
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
Strength    |	1
Dexterity   |	1
Constitution|	1
Wisdom      |	1
Intelligence|	1
Charisma    |	1
Pool        |	66
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
		passed += 4
	else:
		failed.append('hidden1')

# setup methods
def catchOutput(inputs=None, seed=''):
	p = run(f"python3 {file} {seed}", capture_output=True, text=True, shell=True, input=inputs)
	return p.stdout

if __name__ == "__main__":
	main()
