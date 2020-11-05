from subprocess import run, TimeoutExpired, Popen, PIPE
from os import getcwd
file = "scrambler.py"

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
	inputs = "This is my message.\n"
	correct = "What is the message to scramble?\n"
	correct += "There are 4 words in the message.\n"
	result = catchOutput(inputs)[:len(correct)]
	if result == correct:
		score += 1
	
	total += 1
	#def test_2(self):
	inputs = "This is my message. \n"
	correct = "What is the message to scramble?\n"
	correct += "There are 5 words in the message.\n"
	correct += "Here's the shuffled message:\n"
	correct += "my is This  message.\n"
	correct2 += "What is the message to scramble?\nThere are 5 words in the message.\nHere's the shuffeled message:\nmy is This  message.\n"
	result = catchOutput(inputs, '0')
	if result == correct or result == correct2:
		score += 1
	

	#hidden tests
	total += 1
	inputs = "Wacky  multi   space message.\n"
	correct = "What is the message to scramble?\n"
	correct += "There are 7 words in the message.\n"
	correct += "Here's the shuffled message:\n"
	correct += "message. multi   space  Wacky\n"
	correct2 = "What is the message to scramble?\nThere are 7 words in the message.\nHere's the shuffled message:\nmessage. multi   space  Wacky\n"
	result = catchOutput(inputs, '14')
	if result == correct or result == correct2:
		score += 1
	

	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())
