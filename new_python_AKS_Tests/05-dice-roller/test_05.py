import unittest, subprocess

class Tests(unittest.TestCase):
	file = "dice_roller.py"
	
	def test_1(self):
		inputs = "5\n10\n\n"
		correct = "How many dice would you like to roll?\nHow many sides do the dice have?\nPress enter to roll 5x d10.\n"
		result = Tests.catchOutput(inputs)[:len(correct)]
		self.assertEqual(result, correct)
	
	def test_2(self):
		inputs = "3\n4\n0\n"
		correct = "How many dice would you like to roll?\nHow many sides do the dice have?\nPress enter to roll 3x d4.\n"
		correct += "Roll 1: 2\nRoll 2: 1\nRoll 3: 2\n"
		result = Tests.catchOutput(inputs)[:len(correct)]
		self.assertEqual(result, correct)
		
	def test_3(self):
		inputs = "3\n4\n1\n"
		correct = "How many dice would you like to roll?\nHow many sides do the dice have?\nPress enter to roll 3x d4.\n"
		correct += "Roll 1: 2\nRoll 2: 2\nRoll 3: 1\n"
		correct += "Total: 5\n"
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