import unittest, subprocess, sys
from io import StringIO

class Tests(unittest.TestCase):
	file = "hello_world.py"
	original = sys.stdin
	
	def test_1(self):
		correct = "Hello World!\n"
		result = Tests.catchOutput()[:len(correct)]
		self.assertEqual(result, correct)
		
	def test_2(self):
		correct = "Hello World!\nNUAMES\n"
		result = Tests.catchOutput()[:len(correct)]
		self.assertEqual(result, correct)
	
	def test_3(self):
		correct = "Hello World!\nNUAMES\nCS 1030\n"
		result = Tests.catchOutput()
		self.assertEqual(result, correct)

	# setup methods
	@staticmethod
	def catchOutput():
		PIPE = subprocess.PIPE
		cmd = f"python3 {Tests.file}"
		p = subprocess.Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
		out,err = p.communicate()
		if err:
			print(err.decode())
		return out.decode()
	
	@staticmethod
	def setInput(inp):
		sys.stdin = StringIO(inp)
	
	@staticmethod
	def resetInput():
		sys.stdin = Tests.original

if __name__ == '__main__':
	unittest.main()