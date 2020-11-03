from subprocess import run, TimeoutExpired, Popen, PIPE
from os import getcwd
file = "coin_flipper.py"

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
	correct += "The coin was flipped 100 times.\nHeads: 50\tTails: 50\n"
	result = catchOutput(inputs, '0')
	if result == correct:
		score += 1
		
		
	#hidden tests
	total += 1
	inputs = "10\n"
	correct = "How many times do you want to flip the coin?\n"
	correct1 = correct + "The coin was flipped 10 times.\nHeads: 7\tTails: 3\n"
	correct2 = correct + "The coin was flipped 10 times.\nHeads: 3\tTails: 7\n"
	result = catchOutput(inputs, '14')
	if result == correct1 or result == correct2:
		score += 1
	
	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())
