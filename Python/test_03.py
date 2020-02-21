import subprocess
file = "coin_flipper.py"

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
	inputs = "2\n\n"
	correct = "How many times do you want to flip the coin?\n"
	result = catchOutput(inputs)[:len(correct)]
	if result == correct:
		score += 1

	total += 1
	#def test_2(self):
	inputs = "10\n1\n"
	correct = "How many times do you want to flip the coin?\nPress enter to see the results.\n"
	correct += "The coin was flipped 10 times.\nHeads: 5\tTails: 5\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1

	total += 1
	#def test_3(self):
	inputs = "100\n0\n"
	correct = "How many times do you want to flip the coin?\nPress enter to see the results.\n"
	correct += "The coin was flipped 100 times.\nHeads: 50\tTails: 50\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1
		
		
	#hidden tests
	total += 1
	inputs = "10\n14\n"
	correct = "How many times do you want to flip the coin?\nPress enter to see the results.\n"
	correct += "The coin was flipped 10 times.\nHeads: 7\tTails: 3\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1
	
	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())