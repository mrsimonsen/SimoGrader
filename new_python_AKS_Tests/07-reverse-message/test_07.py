import unittest, subprocess

class Tests(unittest.TestCase):
	file = "reverse_message.py"
	
	def test_1(self):
		inputs = "This is my message."
		correct = "What is your message?\n\nYour message reversed is:\n"
		correct += ".egassem ym si sihT\n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)
	
	def test_2(self):
		inputs = "With some   space   . "
		correct = "What is your message?\n\nYour message reversed is:\n"
		correct += " .   ecaps   emos htiW\n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)
		
	# setup methods
	@staticmethod
	def catchOutput(inputs=None):
		p = subprocess.run(["python3", Tests.file], capture_output=True, input=inputs, text=True)
		if err:=p.stderr:
			print(err)
		return p.stdout

if __name__ == '__main__':
	unittest.main()