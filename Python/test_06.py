from subprocess import run
from os import getcwd
file = "counter.py"

# setup methods
def catchOutput(inputs=None, seed=''):
	cwd = getcwd()
	p = run(f"python3 {Tests.file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs)
	return p.stdout

def main():
	total = 0
	score = 0
	total += 1
	#def test_1(self):
	inputs = "1\n10\n2\n"
	correct = "What is the starting number?\nWhat is the ending number?\nHow much should I count by?\nCounting from 1 to 10 by 2:"
	result = catchOutput(inputs)[:len(correct)]
	if result == correct:
		score += 1

	total += 1
	#def test_2(self):
	inputs = "1\n10\n2\n"
	correct = "What is the starting number?\nWhat is the ending number?\nHow much should I count by?\nCounting from 1 to 10 by 2:\n"
	correct += "1 3 5 7 9 \n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1

	total += 1
	#def test_3(self):
	inputs = "3\n1\n-1\n"
	correct = "What is the starting number?\nWhat is the ending number?\nHow much should I count by?\nCounting from 3 to 1 by -1:\n"
	correct += "3 2 1 \n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1
		
	#hidden tests
	total += 1
	inputs = "1\n10\n1\n"
	correct = "What is the starting number?\nWhat is the ending number?\nHow much should I count by?\nCounting from 1 to 10 by 1:\n"
	correct += "1 2 3 4 5 6 7 8 9 10 \n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1
	
	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())