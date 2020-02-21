import unittest, subprocess

class Tests(unittest.TestCase):
	file = "GMN2.py"
	
	def test_1(self):
		inputs = "0\n1\n1\n1\n1\n1\n1\n1\n"
		correct = "\tWelcome to 'Guess My Number 2.0'!\n\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\nPress enter to begin.\n"
		result = Tests.catchOutput(inputs)[:len(correct)]
		self.assertEqual(result, correct)
	
	def test_2(self):
		inputs = "\n1\n1\n1\n1\n1\n1\n1\n"
		correct = "\tWelcome to 'Guess My Number 2.0'!\n\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\nPress enter to begin.\nTake guess number 1:\n"
		result = Tests.catchOutput(inputs)[:len(correct)]
		self.assertEqual(result, correct)
	
	def test_3(self):
		inputs = "0\n47\n"
		correct = "\tWelcome to 'Guess My Number 2.0'!\n\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\nPress enter to begin.\nTake guess number 1:\n"
		correct += "You guessed it! The number was 47.\nAnd it only took you 1 tries!\n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)
	
	def test_4(self):
		inputs = "1\n1\n1\n1\n1\n100\n1\n1\n"
		correct = "\tWelcome to 'Guess My Number 2.0'!\n\nI'm thinking of a number between 1 and 100.\nYou have 6 attempts to guess my number.\nPress enter to begin.\nTake guess number 1:\n"
		correct += "Higher...\nTake guess number 2:\n" 
		correct += "Higher...\nTake guess number 3:\n"
		correct += "Higher...\nTake guess number 4:\n"
		correct += "Higher...\nTake guess number 5:\n"
		correct += "Lower...\nTake guess number 6:\n"
		correct += "You ran out of tries! The number was 62.\n"
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