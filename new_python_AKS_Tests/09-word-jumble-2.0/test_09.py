import unittest, subprocess

class Tests(unittest.TestCase):
	file = "WJ2.py"
	
	def test_1(self):
		seed = '0'
		inputs = "\n"
		correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n(Press the enter key at the prompt to quit.)\n\n"
		correct+= "The jumble is: bjlemu\n\nYour guess:\n"
		correct += "Goodbye.\n"
		result = Tests.catchOutput(inputs, seed)
		self.assertEqual(result, correct)

		
	# setup methods
	@staticmethod
	def catchOutput(inputs=None, seed=''):
		p = subprocess.run(["python3", Tests.file, seed], capture_output=True, input=inputs, text=True)
		if err:=p.stderr:
			print(err)
		return p.stdout

if __name__ == '__main__':
	unittest.main()