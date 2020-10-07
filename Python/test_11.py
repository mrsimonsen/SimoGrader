from subprocess import run
from os import getcwd
file = "guess_AI.py"
import guess_AI
INTRO = "I am a special mind-reading machine and will guess the number you're thinking of between 1 and 100 in 6 tries or less.\nAfter each guess, tell me if I'm 'high', 'low', or 'correct'.\n"

# setup methods
def catchOutput(inputs=None, seed=''):
	cwd = getcwd()
	result = None
	try:
		p = run(f"python3 {file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs, timeout=5)
	except TimeoutExpired:
		result = ""
	else:
		result = p.stdout
	return result

def main():
	total = 0
	score = 0
	total += 1
	
	#def test_1(self):
	inputs = "yo\nLOW\n"
	correct = INTRO
	correct += "For try 1 I guess 47\n"
	correct += "Am I 'high', 'low', or 'correct'?\n"
	correct += "Am I 'high', 'low', or 'correct'?\n"
	result = catchOutput(inputs, '0')[:len(correct)]
	if result == correct:
		score += 1
	
	total += 1
	#def test_2(self):
	#with self.subTest():A
	correct = "I knew I could beat you, and in 6 tries too!\nGoodbye."
	result = guess_AI.end(6, 'correct')
	if result == correct:
		score += 1
	#with self.subTest():B
	total += 1
	correct = "I ran out of tries! You bested me!\nGoodbye."
	result = guess_AI.end(7, 'correct')
	if result == correct:
		score += 1
	#with self.subTest():C
	total += 1
	correct = "I ran out of tries! You bested me!\nGoodbye."
	result = guess_AI.end(3, 'low')
	if result == correct:
		score += 1
		
	total += 1
	#def test_3(self):
	#with self.subTest():A
	if guess_AI.high_low(1,100,50,'high',5,True) == (1,49,6,True):
		score += 1
	total += 1
	#with self.subTest():B
	if guess_AI.high_low(1,100,20,'low',2,True) == (21,100,3,True):
		score += 1
	total += 1
	#with self.subTest():C
	if guess_AI.high_low(1,100,50,'correct',5,True) == (1,100,5,False):
		score += 1
	total += 1
	#with self.subTest():D
	if guess_AI.high_low(1,100,50,'low',6,True) == (1,100,6,False):
		score += 1
		
	#hidden tests
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
		score += 2
	
	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())
