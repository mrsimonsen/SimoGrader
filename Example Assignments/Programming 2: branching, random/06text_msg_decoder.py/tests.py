import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "Some message IDK\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1(self, stdout):
		correct = "Enter text:\nYou entered: Some message IDK\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "IDK if I'll go. It's my BFF's birthday.\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_message_1(self, stdout):
		correct = "Enter text:\nYou entered: IDK if I'll go. It's my BFF's birthday.\n"
		correct += "\tBFF: best friend forever\n\tIDK: I don't know\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "Nice pic, TMI haha JK. TTYL\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_message_2(self, stdout):
		correct = "Enter text:\nYou entered: Nice pic, TMI haha JK. TTYL\n"
		correct += "\tJK: just kidding\n\tTMI: too much information\n\tTTYL: talk to you later\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "TMI BFF JK IDK TTYL\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_all_5(self, stdout):
		correct = "Enter text:\nYou entered: TMI BFF JK IDK TTYL\n"
		correct += "\tBFF: best friend forever\n\tIDK: I don't know\n\tJK: just kidding\n\tTMI: too much information\n\tTTYL: talk to you later\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)


if __name__ == "__main__":
	unittest.main(module='tests', failfast=True)