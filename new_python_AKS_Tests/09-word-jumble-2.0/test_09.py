import unittest
from subprocess import run
from os import getcwd

class Tests(unittest.TestCase):
	file = "WJ2.py"
	
	def test_1(self):
		inputs = "\n"
		correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n(Press the enter key at the prompt to quit.)\n\n"
		correct += "The jumble is: asey\n\nYour guess:\n"
		correct += "Goodbye.\n"
		result = Tests.catchOutput(inputs, '7')
		self.assertEqual(result, correct)
	
	def test_2(self):
		inputs = "blah\n\n"
		correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n(Press the enter key at the prompt to quit.)\n\n"
		correct += "The jumble is: thpoyn\n\nYour guess:\n"
		correct += "Sorry, that's not it.\nType '?' if you want a hint.\n"
		correct += "Your guess:\nGoodbye.\n"
		result = Tests.catchOutput(inputs, '5')
		self.assertEqual(result, correct)
		
	def test_3(self):
		inputs = "?\n\n"
		correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n(Press the enter key at the prompt to quit.)\n\n"
		correct += "The jumble is: bjlemu\n\nYour guess:\n"
		correct += "the name of the game\n"
		correct += "Your guess:\nGoodbye.\n"
		result = Tests.catchOutput(inputs, '0')
		self.assertEqual(result, correct)
		
	def test_4(self):
		inputs="answer\n"
		correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n(Press the enter key at the prompt to quit.)\n\n"
		correct += "The jumble is: anesrw\n\nYour guess:\n"
		correct += "That's it! You guessed it!\n"
		correct += "Good job not using a hint!\n"
		correct += "Thanks for playing.\n"
		result = Tests.catchOutput(inputs, '2')
		self.assertEqual(result, correct)
		
	def test_5(self):
		inputs="?\ndifficult\n"
		correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n(Press the enter key at the prompt to quit.)\n\n"
		correct += "The jumble is: icdultiff\n\nYour guess:\n"
		correct += "not easy\n"
		correct += "Your guess:\n"
		correct += "That's it! You guessed it!\n"
		correct += "Try to not use a hint next time.\n"
		correct += "Thanks for playing.\n"
		result = Tests.catchOutput(inputs, '1')
		self.assertEqual(result, correct)
		
	# setup methods
	@staticmethod
	def catchOutput(inputs=None, seed=''):
		cwd = getcwd()
		p = run(f"python3 {Tests.file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs)
		return p.stdout

if __name__ == '__main__':
	unittest.main()