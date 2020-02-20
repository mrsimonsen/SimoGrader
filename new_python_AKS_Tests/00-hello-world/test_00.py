import unittest
import subprocess

class Tests(unittest.TestCase):
	file = "hello_world.py"
	
	def test_1(self):
		correct = "Hello World!\n"
		result = self.catchOutput()[:len(correct)]
		self.assertEqual(result, correct)
		
	def test_2(self):
		correct = "Hello World!\nNUAMES\n"
		result = self.catchOutput()[:len(correct)]
		self.assertEqual(result, correct)
	
	def test_3(self):
		correct = "Hello World!\nNUAMES\nCS 1030\n"
		result = self.catchOutput()
		self.assertEqual(result, correct)

	# setup method
	def catchOutput(self):
		PIPE = subprocess.PIPE
		cmd = f"python3 {Tests.file}"
		p = subprocess.Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
		out,err = p.communicate()
		if err:
			print(err.decode())
		return out.decode()

if __name__ == '__main__':
	unittest.main()