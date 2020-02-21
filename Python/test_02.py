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
	total += 1
	#def test_1(self):
	inputs = "2\n"
	correct = "Press enter to crack open your cookie and read your fortune.\n"
	correct += "Help! I’m being held prisoner in a fortune cookie bakery!\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1

	total += 1
	#def test_2(self):
	inputs = "1\n"
	correct = "Press enter to crack open your cookie and read your fortune.\n"
	correct += "Cookie said: \"You really crack me up.\"\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1


	total += 1
	#def test_3(self):
	inputs = "7\n"
	correct = "Press enter to crack open your cookie and read your fortune.\n"
	correct += "You are not illiterate.\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1
		
	total += 1	
	#def test_4(self):
	inputs = "0\n"
	correct = "Press enter to crack open your cookie and read your fortune.\n"
	correct += "You will read this and say \"Geez! I could come wp with better fortunes than that!\"\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1
	
	total += 1
	#def test_5(self):
	inputs = "5\n"
	correct = "Press enter to crack open your cookie and read your fortune.\n"
	correct += "This cookie is never gonna give you up, never gonna let your down.\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1
		
	#hidden tests
	#no hidden tests for this assignment
	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())