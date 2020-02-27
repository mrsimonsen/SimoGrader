from subprocess import run
from os import getcwd
file = "pig_latin.py"
import pig_latin
INTRO = 

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
	inputs = "yo\nLOW\n"
	correct = INTRO
	correct += "For try 1 I guess 14\n"
	correct += "Am I 'high', 'low', or 'correct'?\n"
	correct += "Am I 'high', 'low', or 'correct'?\n"
	result = catchOutput(inputs, '14')[:len(correct)]
	if result == correct:
		score += 1
	
			
	#hidden tests
	total += 2
	inputs = ""
	correct = '''
'''
	result = catchOutput(inputs)
	if result == correct:
		score += 2
	
	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())