import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	#unittest.defaultTestLoader.sortTestMethodsUsing = lambda *args: -1
	maxDiff = None
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_2_no_comma(self, stdout):
		correct_out = "Error: No comma in string.\n"
		result_dict = {}
		try:
			student.parse_data("no comma", result_dict)
			result = stdout.getvalue()
			self.assertEqual(result, correct_out)
			self.assertEqual(result_dict, {}, "the origial dictionary should not be changed")
		except AttributeError:
			self.fail("Message: parse_data() function is missing")
		except TypeError:
			self.fail('Message: parse_data() function has incorrect parameters')

	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_2_multiple_commmas(self, stdout):
		correct = "Error: Too many commas in string.\n"
		result_dict = {"some data": 6}
		try:
			student.parse_data("lots,of,commas",result_dict)
			result = stdout.getvalue()
			self.assertEqual(result, correct)
			self.assertEqual(result_dict, {"some data": 6}, "the origial dictionary should not be changed")
		except AttributeError:
			self.fail("Message: parse_data() function is missing")
		except TypeError:
			self.fail('Message: parse_data() function has incorrect parameters')

	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_2_not_int(self, stdout):
		correct = "Error: Comma not followed by an integer.\n"
		result_dict = {'a':1,'b':2}
		try:
			student.parse_data("some,data",result_dict)
			result = stdout.getvalue()
			self.assertEqual(result, correct)
			self.assertEqual(result_dict, {'a':1,'b':2}, "the origial dictionary should not be changed")
		except AttributeError:
			self.fail("Message: parse_data() function is missing")
		except TypeError:
			self.fail('Message: parse_data() function has incorrect parameters')

	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_2(self, stdout):
		correct_out = "Data string: Star Wars\nData integer: 9\n\n"
		result_dict = {'b':2}
		correct_dict = {'b':2,"Star Wars": 9}
		try:
			student.parse_data("  Star Wars , 9 ",result_dict)
			result_out = stdout.getvalue()
			self.assertEqual(result_out, correct_out)
			self.assertEqual(result_dict, correct_dict, "dictionary wasn't edited")
		except AttributeError:
			self.fail("Message: parse_data() function is missing")
		except TypeError:
			self.fail('Message: parse_data() function has incorrect parameters')

	@patch('sys.stdout', new_callable = StringIO)
	def test05_part_3(self, stdout):
		correct = "\n                          a title\ncol1 header         |            col2 header\n--------------------------------------------\na                   |                      1\nb                   |                      2\nc                   |                      3\nd                   |                      4\ne                   |                      5\nf                   |                      6\n"
		dict = {}
		count = 0
		for i in 'abcdef':
			count += 1
			dict[i] = count
		try:
			student.output_table(dict, 'a title', 'col1 header', 'col2 header')
			result = stdout.getvalue()
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: output_table() function is missing")
		except TypeError:
			self.fail('Message: output_table() function has incorrect parameters')


	@patch('sys.stdout', new_callable = StringIO)
	def test06_part_4(self, stdout):
		correct = "                   a *\n                   b **\n                   c ***\n                   d ****\n                   e *****\n                   f ******\n"
		dict = {}
		count = 0
		for i in 'abcdef':
			count += 1
			dict[i] = count
		try:
			student.output_histogram(dict)
			result = stdout.getvalue()
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: output_histogram() function is missing")
		except TypeError:
			self.fail('Message: output_histogram() function has incorrect parameters')


	inputs = "Number of Novels Authored\nAuthor name\nNumber of novels\nJane Austen,6\nCharles Dickens,20\nErnest Hemingway 9\nErnest hemingway9\nErnest Hemingway,9\nJack Kerouac,22\nF, Scott Fitzgerald,8\nF. Scott, Fitzgerald, 8    \nF. Scott Fitzgerald,8\nMary Shelley,7\nCharlotte Bronte,5\nMark Twain,11\nAgatha Christie,seventythree\nAgatha Christie,70three\nAgatha Christie,seventy3\nAgatha Christie,73\nIan Fleming,14\nJ.K. Rowling,14\nStephen King,    54\nOscar Wilde,1\ndone\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test07_all(self, stdout):
		correct = '''Enter a title for the data:
Enter the column 1 header:
Enter the column 2 header:
Enter a data point ('done' to stop input):
Data string: Jane Austen
Data integer: 6

Enter a data point ('done' to stop input):
Data string: Charles Dickens
Data integer: 20

Enter a data point ('done' to stop input):
Error: No comma in string.
Enter a data point ('done' to stop input):
Error: No comma in string.
Enter a data point ('done' to stop input):
Data string: Ernest Hemingway
Data integer: 9

Enter a data point ('done' to stop input):
Data string: Jack Kerouac
Data integer: 22

Enter a data point ('done' to stop input):
Error: Too many commas in string.
Enter a data point ('done' to stop input):
Error: Too many commas in string.
Enter a data point ('done' to stop input):
Data string: F. Scott Fitzgerald
Data integer: 8

Enter a data point ('done' to stop input):
Data string: Mary Shelley
Data integer: 7

Enter a data point ('done' to stop input):
Data string: Charlotte Bronte
Data integer: 5

Enter a data point ('done' to stop input):
Data string: Mark Twain
Data integer: 11

Enter a data point ('done' to stop input):
Error: Comma not followed by an integer.
Enter a data point ('done' to stop input):
Error: Comma not followed by an integer.
Enter a data point ('done' to stop input):
Error: Comma not followed by an integer.
Enter a data point ('done' to stop input):
Data string: Agatha Christie
Data integer: 73

Enter a data point ('done' to stop input):
Data string: Ian Fleming
Data integer: 14

Enter a data point ('done' to stop input):
Data string: J.K. Rowling
Data integer: 14

Enter a data point ('done' to stop input):
Data string: Stephen King
Data integer: 54

Enter a data point ('done' to stop input):
Data string: Oscar Wilde
Data integer: 1

Enter a data point ('done' to stop input):

        Number of Novels Authored
Author name         |       Number of novels
--------------------------------------------
Jane Austen         |                      6
Charles Dickens     |                     20
Ernest Hemingway    |                      9
Jack Kerouac        |                     22
F. Scott Fitzgerald |                      8
Mary Shelley        |                      7
Charlotte Bronte    |                      5
Mark Twain          |                     11
Agatha Christie     |                     73
Ian Fleming         |                     14
J.K. Rowling        |                     14
Stephen King        |                     54
Oscar Wilde         |                      1
         Jane Austen ******
     Charles Dickens ********************
    Ernest Hemingway *********
        Jack Kerouac **********************
 F. Scott Fitzgerald ********
        Mary Shelley *******
    Charlotte Bronte *****
          Mark Twain ***********
     Agatha Christie *************************************************************************
         Ian Fleming **************
        J.K. Rowling **************
        Stephen King ******************************************************
         Oscar Wilde *
'''
		try:
			student.main()
			result = stdout.getvalue()
			self.assertEqual(result, correct)
		except NameError:
			self.fail("Message: this test requires all function to exist before running")

def main(simple):
	suite = unittest.defaultTestLoader
	runner = unittest.TextTestRunner(stream=StringIO(), descriptions=False)
	result = runner.run(suite.loadTestsFromTestCase(Tests))
	total = result.testsRun
	if result.wasSuccessful():
		score = 10
		passed = total
	else:
		passed = total - len(result.failures) - len(result.errors)
		score = round(passed/total*10,2)
	report = f"Passed: {passed}/{total}\nScore: {score}\n"
	if not simple:
		failed = []
		for i in result.failures:
			failed.append(f"Fail: {i[0].id()[15:]}")
		for i in result.errors:
			failed.append(f"Error: {i[0].id()[15:]}")
		report += "Failed:\n"
		for i in failed:
			report += f"\t{i}\n"
		print(report)
	return score

if __name__ == '__main__':
	simple = bool(sys.argv[1])
	score = main(simple)
	with open('score.txt','w') as f:
		f.write(str(score))
