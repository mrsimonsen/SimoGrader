from subprocess import run
from os import getcwd
file = "right_triangle.py"

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
	inputs = "@\n3\n"
	correct = "Enter a character:\nEnter a triangle height:\n"
	correct += "\n@ \n@ @ \n@ @ @ \n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1
		
	total += 1 
	#def test_2(self):
	inputs = "%\n5\n"
	correct = "Enter a character:\nEnter a triangle height:\n"
	correct += "\n% \n% % \n% % % \n% % % % \n% % % % % \n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1
		
	#hidden tests
	total += 1
	inputs = "$\n7\n"
	correct = "Enter a character:\nEnter a triangle height:\n"
	correct += "\n$ \n$ $ \n$ $ $ \n$ $ $ $ \n$ $ $ $ $ \n$ $ $ $ $ $ \n$ $ $ $ $ $ $ \n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1
		
	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())
