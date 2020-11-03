from subprocess import run, TimeoutExpired, Popen, PIPE
from os import getcwd

file = "dice_roller.py"

# setup methods
def catchOutput(inputs=None, seed=''):
	cwd = getcwd()
	result = None
	p = Popen(f"python3 {file} {seed}",stdin=PIPE,stdout=PIPE,shell=True,cwd=cwd, text=True)
	try:
		out = p.communicate(input=inputs, timeout=3)
		result = out[0]
	except TimeoutExpired:
		result = ""
		p.kill()
		run("ps fjx > kill.txt ", shell=True)
		with open('kill.txt','r') as f:
			data = f.readlines()
		k = data[-1].split(" ")
		run(f"kill {k[5]}",shell=True)
	return result

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
	correct += "Total: 6\n"
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
