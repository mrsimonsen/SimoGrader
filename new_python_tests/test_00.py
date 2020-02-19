import unittest
import subprocess

class Tests(unittest.TestCase):
	file = "hello_world.py"
	
	def test_1(self):
		result = self.catchOutput()
		correct = "Hello World!\n"
		self.assertEqual(result, correct)
		
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