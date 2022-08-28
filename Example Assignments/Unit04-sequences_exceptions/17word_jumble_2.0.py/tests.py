import unittest, sys, random
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1(self, stdout):
		correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n\tType '?' if you want a hint.\n\t(Press the enter key at the prompt to quit.)\n\n"
		random.seed(0)
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_2(self, stdout):
		correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n\tType '?' if you want a hint.\n\t(Press the enter key at the prompt to quit.)\n\nThe jumble is: bjlemu\n\nYour guess:\nGoodbye.\n"
		random.seed(0)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "bob\n\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3(self, stdout):
		correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n\tType '?' if you want a hint.\n\t(Press the enter key at the prompt to quit.)\n\nThe jumble is: icdultiff\n\nYour guess:\nSorry, that's not it.\nType '?' if you want a hint.\nYour guess:\nGoodbye.\n"
		random.seed(1)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "bob\n?\n\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_4_difficult(self, stdout):
		correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n\tType '?' if you want a hint.\n\t(Press the enter key at the prompt to quit.)\n\nThe jumble is: icdultiff\n\nYour guess:\nSorry, that's not it.\nType '?' if you want a hint.\nYour guess:\nnot easy\nYour guess:\nGoodbye.\n"
		random.seed(1)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "?\n\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test05_part_4_jumble(self, stdout):
		correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n\tType '?' if you want a hint.\n\t(Press the enter key at the prompt to quit.)\n\nThe jumble is: bjlemu\n\nYour guess:\nthe name of the game\nYour guess:\nGoodbye.\n"
		random.seed(0)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "?\n\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test06_part_4_answer(self, stdout):
		correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n\tType '?' if you want a hint.\n\t(Press the enter key at the prompt to quit.)\n\nThe jumble is: anesrw\n\nYour guess:\nwhat you're looking for\nYour guess:\nGoodbye.\n"
		random.seed(2)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "?\n\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test07_part_4_python(self, stdout):
		correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n\tType '?' if you want a hint.\n\t(Press the enter key at the prompt to quit.)\n\nThe jumble is: thpoyn\n\nYour guess:\na slithery coding language\nYour guess:\nGoodbye.\n"
		random.seed(5)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "?\n\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test08_part_4_easy(self, stdout):
		correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n\tType '?' if you want a hint.\n\t(Press the enter key at the prompt to quit.)\n\nThe jumble is: asey\n\nYour guess:\nnot hard\nYour guess:\nGoodbye.\n"
		random.seed(7)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "easy\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test09_part_5_no_hint(self, stdout):
		correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n\tType '?' if you want a hint.\n\t(Press the enter key at the prompt to quit.)\n\nThe jumble is: asey\n\nYour guess:\nThat's it! You guessed it!\nGood job not using a hint!\nThanks for playing.\n"
		random.seed(7)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "easy\n?\nanswer\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test10_part_5_with_hint(self, stdout):
		correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n\tType '?' if you want a hint.\n\t(Press the enter key at the prompt to quit.)\n\nThe jumble is: anesrw\n\nYour guess:\nSorry, that's not it.\nType '?' if you want a hint.\nYour guess:\nwhat you're looking for\nYour guess:\nThat's it! You guessed it!\nTry to not use a hint next time.\nThanks for playing.\n"
		random.seed(2)
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)


if __name__ == "__main__":
	unittest.main(module='tests', failfast=True)