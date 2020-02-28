import unittest
from subprocess import run
from os import getcwd
import tv_remote

class Tests(unittest.TestCase):
	file = "tv_remote.py"
	MENU = '''
vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit
\n'''
	
	START = "Channel: 3\nVolume: 5\n"

	def test_1(self):
		inputs = "q\n"
		correct = Tests.START + Tests.MENU + "Select an option:\n"
		correct += "Goodbye.\n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)
		
	def test_2(self):
		r = tv_remote.Remote()
		for i in range(6):
			r.volume_up()
		result = r.__str__()
		correct = "Channel: 3\nVolume: 10"
		self.assertEqual(result, correct)
		
	def test_3(self):
		r = tv_remote.Remote()
		for i in range(7):
			r.volume_down()
		result = r.__str__()
		correct = "Channel: 3\nVolume: 0"
		self.assertEqual(result, correct)
		
	def test_4(self):
		r = tv_remote.Remote()
		for i in range(103):
			r.channel_up()
		result = r.__str__()
		correct = "Channel: 6\nVolume: 5"
		self.assertEqual(result, correct)
	
	def test_5(self):
		r = r = tv_remote.Remote()
		for i in range(10):
			r.channel_down()
		result = r.__str__()
		correct = "Channel: 93\nVolume: 5"
		self.assertEqual(result, correct)
		
	def test_6(self):
		inputs = "set\na\nq\n"
		correct = Tests.START + Tests.MENU + "Select an option:\n"
		correct += "What channel?\nError: invalid literal for int() with base 10: 'a'\nExplanation: 'a' isn't a number\n"
		correct += Tests.MENU + "Select an option:\n"
		correct += "Goodbye.\n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)
		
	def test_7(self):
		self.maxDiff = None
		inputs = "set\n3000\nv\nq\n"
		correct = Tests.START + Tests.MENU + "Select an option:\n"
		correct += "What channel?\n'3000' is out of the channel range\n"
		correct += Tests.MENU + "Select an option:\n"
		correct += Tests.START + Tests.MENU + "Select an option:\n"
		correct += "Goodbye.\n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)			
	
# setup methods
	@staticmethod
	def catchOutput(inputs=None, seed=''):
		cwd = getcwd()
		p = run(f"python3 {Tests.file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs)
		return p.stdout

if __name__ == '__main__':
	unittest.main()
