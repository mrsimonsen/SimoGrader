from subprocess import run
from os import getcwd
import sys

import guess_AI
#11p
file = "guess_AI.py"
passed = 0
total = 0
failed = []
INTRO = "I am a special mind-reading machine and will guess the number you're thinking of between 1 and 100 in 6 tries or less.\nAfter each guess, tell me if I'm 'high', 'low', or 'correct'.\n"

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
	hidden1()
	print(f"{passed}/{total}")

def test1():
	global total, passed
	total += 1
	inputs = "yo\nLOW\n"
	correct = INTRO
	correct += "For try 1 I guess 50\n"
	correct += "Am I 'high', 'low', or 'correct'?\n"
	correct += "Am I 'high', 'low', or 'correct'?\n"
	result = catchOutput(inputs, '0')[:len(correct)]
	if result == correct:
		passed += 1
	else:
		failed.append('test1')

def test2():
	global total, passed
	total += 1
	correct = "I knew I could beat you, and in 6 tries too!\nGoodbye."
	result = guess_AI.end(6, 'correct')
	if result == correct:
		passed += 1
	else:
		failed.append('test2')

def test3():
	global total, passed
	total += 1
	correct = "I ran out of tries! You bested me!\nGoodbye."
	result = guess_AI.end(7, 'correct')
	if result == correct:
		passed += 1
	else:
		failed.append('test3')

def test4():
	global total, passed
	total += 1
	correct = "I ran out of tries! You bested me!\nGoodbye."
	result = guess_AI.end(3, 'low')
	if result == correct:
		passed += 1
	else:
		failed.append('test4')

def test5():
	global total, passed
	total += 1
	if guess_AI.high_low(1,100,50,'high',5,True) == (1,49,6,True):
		passed += 1
	else:
		failed.append('test5')

def test6():
	global total, passed
	total += 1
	if guess_AI.high_low(1,100,20,'low',2,True) == (21,100,3,True):
		passed += 1
	else:
		failed.append('test6')

def test7():
	global total, passed
	total += 1
	#with self.subTest():C
	if guess_AI.high_low(1,100,50,'correct',5,True) == (1,100,5,False):
		passed += 1
	else:
		failed.append('test7')

def test8():
	global total, passed
	total += 1
	if guess_AI.high_low(1,100,50,'low',6,True) == (1,100,6,False):
		passed += 1
	else:
		failed.append('test8')

def hidden1():
	global total, passed
	total += 2
	inputs = "LOW\nHIGH\nhigh\nlow\ncorrect\n"
	correct = '''I am a special mind-reading machine and will guess the number you're thinking of between 1 and 100 in 6 tries or less.
After each guess, tell me if I'm 'high', 'low', or 'correct'.
For try 1 I guess 10
Am I 'high', 'low', or 'correct'?
For try 2 I guess 38
Am I 'high', 'low', or 'correct'?
For try 3 I guess 15
Am I 'high', 'low', or 'correct'?
For try 4 I guess 13
Am I 'high', 'low', or 'correct'?
For try 5 I guess 14
Am I 'high', 'low', or 'correct'?
I knew I could beat you, and in 5 tries too!
Goodbye.
'''
	result = catchOutput(inputs, '32')
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
