import unittest, subprocess

class Tests(unittest.TestCase):
	file = "coin_flipper.py"
	
	def test_1(self):
		inputs = "2\n\n"
		correct = "How many times do you want to flip the coin?\n"
		result = Tests.catchOutput(inputs)[:len(correct)]
		self.assertEqual(result, correct)

	def test_2(self):
		inputs = "10\n1\n"
		correct = "How many times do you want to flip the coin?\nPress enter to see the results.\n"
		correct += "The coin was flipped 10 times.\nHeads: 5\tTails: 5\n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)
	
	def test_3(self):
		inputs = "100\n0\n"
		correct = "How many times do you want to flip the coin?\nPress enter to see the results.\n"
		correct += "The coin was flipped 100 times.\nHeads: 50\tTails: 50\n"
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