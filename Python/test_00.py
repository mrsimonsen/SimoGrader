import subprocess
file = "hello_world.py"

# setup methods
def catchOutput(inputs=None):
		p = subprocess.run(["python3", file], capture_output=True, input=inputs, text=True)
		if err:=p.stderr:
			print(err)
		return p.stdout

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