from subprocess import run
from os import getcwd
file = "fortune_cookie.py"

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
	#def test_1(self):
	correct = "You crack open your cookie and your fortune falls out:\n"
	correct1 = correct + "Help! I'm being held prisoner in a fortune cookie bakery!\n"
	correct2 = correct + "Help! I’m being held prisoner in a fortune cookie bakery!\n"
	result = catchOutput(seed = "2")
	if result == correct1 or result == correct2:
		score += 1

	total += 1
	#def test_2(self):
	correct = "You crack open your cookie and your fortune falls out:\n"
	correct += "Cookie said: \"You really crack me up.\"\n"
	result = catchOutput(seed = "1")
	if result == correct:
		score += 1

	total += 1
	#def test_3(self):
	correct = "You crack open your cookie and your fortune falls out:\n"
	correct += "You are not illiterate.\n"
	result = catchOutput(seed = "7")
	if result == correct:
		score += 1
		
	total += 1	
	#def test_4(self):
	correct = "You crack open your cookie and your fortune falls out:\n"
	correct1 = correct + "You will read this and say \"Geez! I could come up with better fortunes than that!\"\n"
	correct2 = correct + "You will read this and say \"Geez! I could come wp with better fortunes than that!\"\n"
	result = catchOutput(seed = "0")
	if result == correct1 or result == correct2:
		score += 1
	
	total += 1
	#def test_5(self):
	correct = "You crack open your cookie and your fortune falls out:\n"
	correct1 = correct + "This cookie is never gonna give you up, never gonna let you down.\n"
	correct2 = correct + "This cookie is never gonna give you up, never gonna let your down.\n"
	result = catchOutput(seed = "5")
	if result == correct1 or result == correct2:
		score += 1
		
	#hidden tests
	#no hidden tests for this assignment
	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())
