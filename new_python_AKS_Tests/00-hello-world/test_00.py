import unittest, subprocess

class Tests(unittest.TestCase):
	file = "hello_world.py"
	
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
	def catchOutput(inputs=None):
		p = subprocess.run(["python3",Tests.file], shell=True, capture_output=True,input=inputs, text=True)
		if err:=p.stderr:
			print(err)
		return p.stdout

if __name__ == '__main__':
	unittest.main()
