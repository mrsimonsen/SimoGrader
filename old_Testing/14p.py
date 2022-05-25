from subprocess import run
from os import getcwd
import sys

import tv_remote

#00p
file = "tv_remote.py"
passed = 0
total = 0
failed = []
MENU = '''
vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit
\n'''
START = "Channel: 3\nVolume: 5\n"

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
	hidden1()
	print(f"{passed}/{total}")

def test1():
	global total, passed
	total += 1
	inputs = "q\n"
	correct = START + MENU + "Select an option:\n"
	correct += "Goodbye.\n"
	result = catchOutput(inputs)
	if result == correct:
		passed += 1
	else:
		failed.append('test1')

def test2():
	global total, passed
	total += 1
	x = None
	r = tv_remote.Remote()
	try:
		x = r._Remote__channel
	except:
		pass
	if x == 3:
		passed += 1
	else:
		failed.append('test2')

def test3():
	global total, passed
	total += 1
	r = tv_remote.Remote()
	x = None
	try:
		x = r.volume
	except:
		pass
	if x == None:
		passed += 1
	else:
		failed.append('test3')

def test4():
	global total, passed
	total += 1
	r = tv_remote.Remote()
	for i in range(6):
		r.volume_up()
	result = r.__str__()
	correct = "Channel: 3\nVolume: 10"
	if result == correct:
		passed += 1
	else:
		failed.append('test4')

def test5():
	global total, passed
	total += 1
	r = tv_remote.Remote()
	for i in range(7):
		r.volume_down()
	result = r.__str__()
	correct = "Channel: 3\nVolume: 0"
	if result == correct:
		passed += 1
	else:
		failed.append('test5')

def test6():
	global total, passed
	total += 1
	r = tv_remote.Remote()
	for i in range(103):
		r.channel_up()
	result = r.__str__()
	correct = "Channel: 6\nVolume: 5"
	if result == correct:
		passed += 1
	else:
		failed.append('test6')

def test7():
	global total, passed
	total += 1
	r = tv_remote.Remote()
	for i in range(10):
		r.channel_down()
	result = r.__str__()
	correct = "Channel: 93\nVolume: 5"
	if result == correct:
		passed += 1
	else:
		failed.append('test7')

def test8():
	global total, passed
	total += 1
	inputs = "set\na\nq\n"
	correct = START + MENU + "Select an option:\n"
	correct += "What channel?\nError: invalid literal for int() with base 10: 'a'\nExplanation: 'a' isn't a number\n"
	correct += MENU + "Select an option:\n"
	correct += "Goodbye.\n"
	result = catchOutput(inputs)
	if result == correct:
		passed += 1
	else:
		failed.append('test8')

def test9():
	global total, passed
	total += 1
	inputs = "set\n3000\nv\nq\n"
	correct = START + MENU + "Select an option:\n"
	correct += "What channel?\n'3000' is out of the channel range\n"
	correct += MENU + "Select an option:\n"
	correct += START + MENU + "Select an option:\n"
	correct += "Goodbye.\n"
	result = catchOutput(inputs)
	if result == correct:
		passed += 1
	else:
		failed.append('test9')

def hidden1():
	global total, passed
	total += 2
	inputs = "set\n30\nvu\nvu\nvd\ncd\ncd\ncu\nv\nq\n"
	correct ='''Channel: 3
Volume: 5

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:
What channel?

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:
Channel: 29
Volume: 6

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:
Goodbye.
'''
	result = catchOutput(inputs)
	if result == correct:
		passed += 2
	else:
		failed.append('hidden1')

# setup methods
def catchOutput(inputs=None, seed=''):
	p = run(f"python3 {file} {seed}", capture_output=True, text=True, shell=True, input=inputs)
	return p.stdout

if __name__ == "__main__":
	main()
