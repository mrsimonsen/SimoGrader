from subprocess import run
from os import getcwd

file = "dice_roller.py"

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
	inputs = "5\n10\n"
	correct = "How many dice would you like to roll?\nHow many sides do the dice have?\nRolling 5x d10.\n"
	result = catchOutput(inputs)[:len(correct)]
	if result == correct:
		score += 1

	total += 1
	#def test_2(self):
	inputs = "3\n4\n"
	correct = "How many dice would you like to roll?\nHow many sides do the dice have?\nRolling 3x d4.\n"
	correct += "Roll 1: 4\nRoll 2: 4\nRoll 3: 1\n"
	result = catchOutput(inputs, '0')[:len(correct)]
	if result == correct:
		score += 1

	total += 1
	#def test_3(self):
	inputs = "3\n4\n"
	correct = "How many dice would you like to roll?\nHow many sides do the dice have?\nRolling 3x d4.\n"
	correct += "Roll 1: 2\nRoll 2: 1\nRoll 3: 3\n"
	correct += "Total: 5\n"
	result = catchOutput(inputs, '1')
	if result == correct:
		score += 1
		
	#hidden tests
	total += 1
	inputs = "5\n20\n"
	correct = "How many dice would you like to roll?\nHow many sides do the dice have?\nRolling 5x d20.\n"
	correct += "Roll 1: 4\nRoll 2: 20\nRoll 3: 17\nRoll 4: 8\nRoll 5: 9\n"
	correct += "Total: 58\n"
	result = catchOutput(inputs, '14')
	if result == correct:
		score += 1
	
	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())
