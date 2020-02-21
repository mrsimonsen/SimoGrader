import unittest, subprocess

class Tests(unittest.TestCase):
	file = "fortune_cookie.py"
	
	def test_1(self):
		inputs = "2\n"
		correct = "Press enter to crack open your cookie and read your fortune.\n"
		correct += "Help! I’m being held prisoner in a fortune cookie bakery!\n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)

	def test_2(self):
		inputs = "1\n"
		correct = "Press enter to crack open your cookie and read your fortune.\n"
		correct += "Cookie said: \"You really crack me up.\"\n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)
	
	def test_3(self):
		inputs = "7\n"
		correct = "Press enter to crack open your cookie and read your fortune.\n"
		correct += "You are not illiterate.\n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)
	
	def test_4(self):
		inputs = "0\n"
		correct = "Press enter to crack open your cookie and read your fortune.\n"
		correct += "You will read this and say \"Geez! I could come wp with better fortunes than that!\"\n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)
		
	def test_5(self):
		inputs = "5\n"
		correct = "Press enter to crack open your cookie and read your fortune.\n"
		correct += "This cookie is never gonna give you up, never gonna let your down.\n"
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