from subprocess import run
from os import getcwd
file = "hello_world.py"

# setup methods
def catchOutput(inputs=None, seed=''):
	cwd = getcwd()
	result = None
	try:
		p = run(f"python3 {file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs, timeout=5)
	except TimeoutExpired:
		result = ""
	else:
		result = p.stdout
	return result

def main():
	total = 0
	score = 0
	total += 1
	#def test_1():
	correct = "Hello World!\n"
	result = catchOutput()[:len(correct)]
	if result == correct:
		score += 1

	total += 1
	#def test_2():
	correct = "Hello World!\nNUAMES\n"
	result = catchOutput()[:len(correct)]
	if result == correct:
		score += 1

	total += 1
	#def test_3():
	correct = "Hello World!\nNUAMES\nCS 1030\n"
	result = catchOutput()
	if result == correct:
		score += 1
		
	#hidden tests
	#no hidden tests for this assignment

	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())