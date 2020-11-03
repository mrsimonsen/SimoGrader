from subprocess import run, TimeoutExpired, Popen, PIPE
from os import getcwd
file = "reverse_message.py"

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
	inputs = "This is my message."
	correct = "What is your message?\n\nYour message reversed is:\n"
	correct += ".egassem ym si sihT\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1
		
	total += 1 
	#def test_2(self):
	inputs = "With some   space   . "
	correct = "What is your message?\n\nYour message reversed is:\n"
	correct += " .   ecaps   emos htiW\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1
		
	#hidden tests
	total += 1
	inputs = "	because	I	tab"
	correct = "What is your message?\n\nYour message reversed is:\n"
	correct += "bat	I	esuaceb	\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1
		
	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())
