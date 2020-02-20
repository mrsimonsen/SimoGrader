import subprocess, sys
from io import StringIO
original = sys.stdin
file = "hello_world.py"

# setup methods
def catchOutput():
	PIPE = subprocess.PIPE
	cmd = f"python3 {file}"
	p = subprocess.Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
	out,err = p.communicate()
	if err:
		print(err.decode())
	return out.decode()

def setInput(inp):
	sys.stdin = StringIO(inp)
	
def resetInput():
	sys.stdin = original


def main():
	total = 0
	score = 0
	#def test_1():
	total += 1
	correct = "Hello World!\n"
	result = catchOutput()[:len(correct)]
	if result == correct:
		score += 1

	#def test_2():
	total += 1
	correct = "Hello World!\nNUAMES\n"
	result = catchOutput()[:len(correct)]
	if result == correct:
		score += 1

	#def test_3():
	total += 1
	correct = "Hello World!\nNUAMES\nCS 1030\n"
	result = catchOutput()
	if result == correct:
		score += 1

	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())