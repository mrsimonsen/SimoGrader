from subprocess import run
from os import getcwd
file = "scrambler.py"

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
	correct += "Here's the shuffeled message:\n"
	correct += "my is This  message.\n"
	result = catchOutput(inputs, '0')
	if result == correct:
		score += 1
	

	#hidden tests
	total += 1
	inputs = "Wacky  multi   space message.\n"
	correct = "What is the message to scramble?\n"
	correct += "There are 7 words in the message.\n"
	correct += "Here's the shuffeled message:\n"
	correct += "message. multi   space  Wacky\n"
	result = catchOutput(inputs, '14')
	if result == correct:
		score += 1
	

	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())