from subprocess import run
from os import getcwd
file = "reverse_message.py"

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
