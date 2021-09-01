from subprocess import run
from os import getcwd
file = "coin_flipper.py"

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
	inputs = "2\n"
	correct = "How many times do you want to flip the coin?\n"
	result = catchOutput(inputs)[:len(correct)]
	if result == correct:
		score += 1

	total += 1
	#def test_2(self):
	inputs = "10\n"
	correct = "How many times do you want to flip the coin?\n"
	correct += "The coin was flipped 10 times.\nHeads: 5\tTails: 5\n"
	result = catchOutput(inputs, '1')
	if result == correct:
		score += 1

	total += 1
	#def test_3(self):
	inputs = "100\n"
	correct = "How many times do you want to flip the coin?\n"
	correct1 = correct + "The coin was flipped 100 times.\nHeads: 40\tTails: 60\n"
	correct2 = correct + "The coin was flipped 100 times.\nHeads: 60\tTails: 40\n"
	result = catchOutput(inputs, '9')
	if (result == correct1) or (result == correct2):
		score += 1
		
		
	#hidden tests
	total += 1
	inputs = "10\n"
	correct = "How many times do you want to flip the coin?\n"
	correct1 = correct + "The coin was flipped 10 times.\nHeads: 3\tTails: 7\n"
	correct2 = correct + "The coin was flipped 10 times.\nHeads: 7\tTails: 3\n"
	result = catchOutput(inputs, '14')
	if (result == correct1) or (result == correct2):
		score += 1

	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())
