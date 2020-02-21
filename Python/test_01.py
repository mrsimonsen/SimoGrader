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
	#def test_1(self):
	total += 1
	inputs = "1\n2\n"
	correct = "Enter a number:\nEnter a second number:\nDoing math for 1 and 2.\n"
	result = catchOutput(inputs)[:len(correct)]
	if result == correct:
		score += 1

	#def test_2(self):
	total += 1
	inputs = "1\n2\n"
	correct = "Enter a number:\nEnter a second number:\nDoing math for 1 and 2.\n"
	correct += "\nAddition = 3\nSubtraction = -1\nMultiplication = 2\nExponent = 1\nDivision = 0.5\nFloor Division = 0\nModulus Division = 1\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1


	#def test_3(self):
	total += 1
	inputs = "1\n16\n"
	correct = "Enter a number:\nEnter a second number:\nDoing math for 1 and 16.\n"
	correct+="\nAddition = 17\nSubtraction = -15\nMultiplication = 16\nExponent = 1\nDivision = 0.062\nFloor Division = 0\nModulus Division = 1\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1
		
	#hidden tests
	total += 1
	inputs = "23\n16\n"
	correct = "Enter a number:\nEnter a second number:\nDoing math for 23 and 16.\n"
	correct+="\nAddition = 39\nSubtraction = 7\nMultiplication = 368\nExponent = 6132610415680998648961\nDivision = 1.438\nFloor Division = 1\nModulus Division = 7\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1

	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())