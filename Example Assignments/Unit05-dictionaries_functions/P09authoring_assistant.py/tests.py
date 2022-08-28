import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "q\n6\n0\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_2(self, stdout):
		correct_out = "\nSample text: \"May the force be with you!\"\nMENU\n1 - Replace all !'s\n2 - Shorten spaces\n3 - Number of non-whitespace characters\n4 - Number of words\n5 - Find text\n0 - Quit\n\nChoose an option:\nThat wasn't a number.\nChoose an option:\nChoose an option:\n"
		correct_return = 0
		try:
			result_return = student.print_menu("May the force be with you!")
			result_out = stdout.getvalue()
			self.assertEqual(result_return, correct_return)
			self.assertEqual(result_out, correct_out)
		except AttributeError:
			self.fail("Message: print_menu() function is missing or doesn't return correctly")
		except TypeError:
			self.fail('Message: print_menu() function has incorrect parameters')

	def test02_part_3(self):
		correct = "May the force be with you."
		try:
			result = student.replace_exclamation("May the force be with you!")
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: replace_exclamation() function is missing or doesn't return correctly")
		except TypeError:
			self.fail('Message: replace_exclamation() function has incorrect parameters')

	def test03_part_4(self):
		correct = "May the force be with you!"
		try:
			result = student.shorten_space("   May   the force   be with you!  ")
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: shorten_space() function is missing or doesn't return correctly")
		except TypeError:
			self.fail('Message: shorten_space() function has incorrect parameters')

	def test04_part_5(self):
		correct = 21
		try:
			result = student.num_non_ws("   May   the force   be with you!  ")
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: num_non_ws() function is missing or doesn't return correctly")
		except TypeError:
			self.fail('Message: num_non_ws() function has incorrect parameters')

	def test05_part_6(self):
		correct = 6
		try:
			result = student.num_words("   May   the force   be with you!  ")
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: num_words() function is missing or doesn't return correctly")
		except TypeError:
			self.fail('Message: num_words() function has incorrect parameters')

	def test06_part_7(self):
		correct = 3
		try:
			result = student.find_text("e ","   May   the force   be with you!  ")
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: find_text() function is missing or doesn't return correctly")
		except TypeError:
			self.fail('Message: find_text() function has incorrect parameters')

	inputs = "  This   is sample! text! \n1\n2\n3\n4\n5\nis \na\n6\n0\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test07_part_1(self, stdout):
		self.maxDiff = None
		correct = "Enter sample text:\n\nSample text: \"  This   is sample! text! \"\nMENU\n1 - Replace all !'s\n2 - Shorten spaces\n3 - Number of non-whitespace characters\n4 - Number of words\n5 - Find text\n0 - Quit\n\nChoose an option:\nEdited text:   This   is sample. text. \n\nSample text: \"  This   is sample. text. \"\nMENU\n1 - Replace all !'s\n2 - Shorten spaces\n3 - Number of non-whitespace characters\n4 - Number of words\n5 - Find text\n0 - Quit\n\nChoose an option:\nEdited text: This is sample. text.\n\nSample text: \"This is sample. text.\"\nMENU\n1 - Replace all !'s\n2 - Shorten spaces\n3 - Number of non-whitespace characters\n4 - Number of words\n5 - Find text\n0 - Quit\n\nChoose an option:\nNumber of non-whitespace characters: 18\n\nSample text: \"This is sample. text.\"\nMENU\n1 - Replace all !'s\n2 - Shorten spaces\n3 - Number of non-whitespace characters\n4 - Number of words\n5 - Find text\n0 - Quit\n\nChoose an option:\nNumber of words: 4\n\nSample text: \"This is sample. text.\"\nMENU\n1 - Replace all !'s\n2 - Shorten spaces\n3 - Number of non-whitespace characters\n4 - Number of words\n5 - Find text\n0 - Quit\n\nChoose an option:\nEnter a word or phrase to be found:\n\"is \" instances: 2\n\nSample text: \"This is sample. text.\"\nMENU\n1 - Replace all !'s\n2 - Shorten spaces\n3 - Number of non-whitespace characters\n4 - Number of words\n5 - Find text\n0 - Quit\n\nChoose an option:\nThat wasn't a number.\nChoose an option:\nChoose an option:\n"
		try:
			student.main()
			result = stdout.getvalue()
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: all other functions must be defined before this test")


if __name__ == "__main__":
	unittest.main(module='tests', failfast=True)