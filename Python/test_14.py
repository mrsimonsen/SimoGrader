from subprocess import run, TimeoutExpired, Popen, PIPE
from os import getcwd
file = "tv_remote.py"
import tv_remote
MENU = '''
vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit
\n'''
START = "Channel: 3\nVolume: 5\n"

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
	#def test_1(self):
	inputs = "q\n"
	correct = START + MENU + "Select an option:\n"
	correct += "Goodbye.\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1
	
	total += 1
	#def test_2(self):
	r = tv_remote.Remote()
	for i in range(6):
		r.volume_up()
	result = r.__str__()
	correct = "Channel: 3\nVolume: 10"
	if result == correct:
		score += 1
		
	total += 1
	#def test_3(self):
	r = tv_remote.Remote()
	for i in range(7):
		r.volume_down()
	result = r.__str__()
	correct = "Channel: 3\nVolume: 0"
	if result == correct:
		score += 1
	
	total += 1
	#def test_4(self):
	r = tv_remote.Remote()
	for i in range(103):
		r.channel_up()
	result = r.__str__()
	correct = "Channel: 6\nVolume: 5"
	if result == correct:
		score += 1
		
	total += 1
	#def test_5(self):
	r = r = tv_remote.Remote()
	for i in range(10):
		r.channel_down()
	result = r.__str__()
	correct = "Channel: 93\nVolume: 5"
	if result == correct:
		score += 1
		
	total += 1
	#def test_6(self):
	inputs = "set\na\nq\n"
	correct = START + MENU + "Select an option:\n"
	correct += "What channel?\nError: invalid literal for int() with base 10: 'a'\nExplanation: 'a' isn't a number\n"
	correct += MENU + "Select an option:\n"
	correct += "Goodbye.\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1
	
	total += 1
	#def test_7(self):
	inputs = "set\n3000\nv\nq\n"
	correct = START + MENU + "Select an option:\n"
	correct += "What channel?\n'3000' is out of the channel range\n"
	correct += MENU + "Select an option:\n"
	correct += START + MENU + "Select an option:\n"
	correct += "Goodbye.\n"
	result = catchOutput(inputs)
	if result == correct:
		score += 1
	
	#hidden tests	
	total += 2
	inputs = "set\n30\nvu\nvu\nvd\ncd\ncd\ncu\nv\nq\n"
	correct ='''Channel: 3
Volume: 5

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:
What channel?

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:
Channel: 29
Volume: 6

vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit

Select an option:
Goodbye.
'''
	result = catchOutput(inputs)
	if result == correct:
		score += 2
		
	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())