import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	maxDiff = None
	inputs = "1\n1\n2\n2\n3\n3\n4\n4\n5\n5\nq"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1_2D_list(self, stdout):
		correct = [[1,1],[2,2],[3,3],[4,4],[5,5]]
		result = student.main()
		self.assertEqual(result, correct, "players list need to be a 2D list")

	inputs = "1\n1\n2\n2\n3\n3\n4\n4\n5\n5\nq"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_1(self, stdout):
		correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n\nROSTER\nPlayer 1 -- Jersey number: 1, Rating: 1\nPlayer 2 -- Jersey number: 2, Rating: 2\nPlayer 3 -- Jersey number: 3, Rating: 3\nPlayer 4 -- Jersey number: 4, Rating: 4\nPlayer 5 -- Jersey number: 5, Rating: 5\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "1\n1\n2\n2\n3\n3\n4\n4\n5\n5\nq"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_2(self, stdout):
		correct = "\nMENU\no - Output roster\na - Output players above a rating\nu - Update player rating\nr - Replace player\nq - Quit\n\nChoose an option:\n"
		student.main()
		result = stdout.getvalue()[497:]
		self.assertEqual(result, correct)

	inputs = "1\n1\n2\n2\n3\n3\n4\n4\n5\n5\no\nq"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_3(self, stdout):
		correct = "ROSTER\nPlayer 1 -- Jersey number: 1, Rating: 1\nPlayer 2 -- Jersey number: 2, Rating: 2\nPlayer 3 -- Jersey number: 3, Rating: 3\nPlayer 4 -- Jersey number: 4, Rating: 4\nPlayer 5 -- Jersey number: 5, Rating: 5\n\nMENU\no - Output roster\na - Output players above a rating\nu - Update player rating\nr - Replace player\nq - Quit\n\nChoose an option:\n"
		student.main()
		result = stdout.getvalue()[627:]
		self.assertEqual(result, correct)

	inputs = "1\n5\n2\n6\n3\n3\n4\n7\n5\n5\na\n5\nq"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test05_part_4(self, stdout):
		correct = "Enter a rating:\n\nABOVE 5\nPlayer 2 -- Jersey number: 2, Rating: 6\nPlayer 4 -- Jersey number: 4, Rating: 7\n\nMENU\no - Output roster\na - Output players above a rating\nu - Update player rating\nr - Replace player\nq - Quit\n\nChoose an option:\n"
		student.main()
		result = stdout.getvalue()[627:]
		self.assertEqual(result, correct)

	inputs = "1\n5\n2\n6\n3\n3\n4\n7\n5\n5\na\n10\nq"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test06_part_4_empty(self, stdout):
		correct = "Enter a rating:\n\nABOVE 10\n\nMENU\no - Output roster\na - Output players above a rating\nu - Update player rating\nr - Replace player\nq - Quit\n\nChoose an option:\n"
		student.main()
		result = stdout.getvalue()[627:]
		self.assertEqual(result, correct)

	inputs = "1\n5\n2\n6\n3\n3\n4\n7\n5\n5\nu\n1\n10\no\nq"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test07_part_5(self, stdout):
		correct = "Enter a jersey number:\nEnter a new rating for player:\n\nMENU\no - Output roster\na - Output players above a rating\nu - Update player rating\nr - Replace player\nq - Quit\n\nChoose an option:\nROSTER\nPlayer 1 -- Jersey number: 1, Rating: 10\nPlayer 2 -- Jersey number: 2, Rating: 6\nPlayer 3 -- Jersey number: 3, Rating: 3\nPlayer 4 -- Jersey number: 4, Rating: 7\nPlayer 5 -- Jersey number: 5, Rating: 5\n\nMENU\no - Output roster\na - Output players above a rating\nu - Update player rating\nr - Replace player\nq - Quit\n\nChoose an option:\n"
		student.main()
		result = stdout.getvalue()[627:]
		self.assertEqual(result, correct)

	inputs = "1\n5\n2\n6\n3\n3\n4\n7\n5\n5\nu\n10\n10\no\nq"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test08_part_5_missing_jersey(self, stdout):
		correct = "Enter a jersey number:\nEnter a new rating for player:\n\nMENU\no - Output roster\na - Output players above a rating\nu - Update player rating\nr - Replace player\nq - Quit\n\nChoose an option:\nROSTER\nPlayer 1 -- Jersey number: 1, Rating: 5\nPlayer 2 -- Jersey number: 2, Rating: 6\nPlayer 3 -- Jersey number: 3, Rating: 3\nPlayer 4 -- Jersey number: 4, Rating: 7\nPlayer 5 -- Jersey number: 5, Rating: 5\n\nMENU\no - Output roster\na - Output players above a rating\nu - Update player rating\nr - Replace player\nq - Quit\n\nChoose an option:\n"
		student.main()
		result = stdout.getvalue()[627:]
		self.assertEqual(result, correct)

	inputs = "1\n5\n2\n6\n3\n3\n4\n7\n5\n5\nr\n3\n16\n5\no\nq"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test09_part_6(self, stdout):
		correct = "Enter a jersey number:\nEnter a new jersey number:\nEnter a rating for the new player:\n\nMENU\no - Output roster\na - Output players above a rating\nu - Update player rating\nr - Replace player\nq - Quit\n\nChoose an option:\nROSTER\nPlayer 1 -- Jersey number: 1, Rating: 5\nPlayer 2 -- Jersey number: 2, Rating: 6\nPlayer 3 -- Jersey number: 16, Rating: 5\nPlayer 4 -- Jersey number: 4, Rating: 7\nPlayer 5 -- Jersey number: 5, Rating: 5\n\nMENU\no - Output roster\na - Output players above a rating\nu - Update player rating\nr - Replace player\nq - Quit\n\nChoose an option:\n"
		student.main()
		result = stdout.getvalue()[627:]
		self.assertEqual(result, correct)

	inputs = "1\n5\n2\n6\n3\n3\n4\n7\n5\n5\nr\n10\no\nq"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test10_part_6_missing_player(self, stdout):
		correct = "Enter a jersey number:\n\nMENU\no - Output roster\na - Output players above a rating\nu - Update player rating\nr - Replace player\nq - Quit\n\nChoose an option:\nROSTER\nPlayer 1 -- Jersey number: 1, Rating: 5\nPlayer 2 -- Jersey number: 2, Rating: 6\nPlayer 3 -- Jersey number: 3, Rating: 3\nPlayer 4 -- Jersey number: 4, Rating: 7\nPlayer 5 -- Jersey number: 5, Rating: 5\n\nMENU\no - Output roster\na - Output players above a rating\nu - Update player rating\nr - Replace player\nq - Quit\n\nChoose an option:\n"
		student.main()
		result = stdout.getvalue()[627:]
		self.assertEqual(result, correct)

	inputs = "84\n7\n23\n4\n4\n5\n30\n2\n66\n9\nu\n30\n10\nr\n10\nr\n4\n14\n1\na\n4\no\nq"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test11_whole_thing(self, stdout):
		correct = "Enter player 1's jersey number:\nEnter player 1's rating:\n\nEnter player 2's jersey number:\nEnter player 2's rating:\n\nEnter player 3's jersey number:\nEnter player 3's rating:\n\nEnter player 4's jersey number:\nEnter player 4's rating:\n\nEnter player 5's jersey number:\nEnter player 5's rating:\n\nROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 4, Rating: 5\nPlayer 4 -- Jersey number: 30, Rating: 2\nPlayer 5 -- Jersey number: 66, Rating: 9\n\nMENU\no - Output roster\na - Output players above a rating\nu - Update player rating\nr - Replace player\nq - Quit\n\nChoose an option:\nEnter a jersey number:\nEnter a new rating for player:\n\nMENU\no - Output roster\na - Output players above a rating\nu - Update player rating\nr - Replace player\nq - Quit\n\nChoose an option:\nEnter a jersey number:\n\nMENU\no - Output roster\na - Output players above a rating\nu - Update player rating\nr - Replace player\nq - Quit\n\nChoose an option:\nEnter a jersey number:\nEnter a new jersey number:\nEnter a rating for the new player:\n\nMENU\no - Output roster\na - Output players above a rating\nu - Update player rating\nr - Replace player\nq - Quit\n\nChoose an option:\nEnter a rating:\n\nABOVE 4\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 4 -- Jersey number: 30, Rating: 10\nPlayer 5 -- Jersey number: 66, Rating: 9\n\nMENU\no - Output roster\na - Output players above a rating\nu - Update player rating\nr - Replace player\nq - Quit\n\nChoose an option:\nROSTER\nPlayer 1 -- Jersey number: 84, Rating: 7\nPlayer 2 -- Jersey number: 23, Rating: 4\nPlayer 3 -- Jersey number: 14, Rating: 1\nPlayer 4 -- Jersey number: 30, Rating: 10\nPlayer 5 -- Jersey number: 66, Rating: 9\n\nMENU\no - Output roster\na - Output players above a rating\nu - Update player rating\nr - Replace player\nq - Quit\n\nChoose an option:\n"
		correct_list = [[84,7],[23,4],[14,1],[30,10],[66,9]]
		result_list = student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)
		self.assertEqual(result_list, correct_list)


if __name__ == "__main__":
	unittest.main(module='tests', failfast=True)