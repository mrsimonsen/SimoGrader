from subprocess import run, TimeoutExpired, Popen, PIPE
from os import getcwd
file = "hello_world.py"

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