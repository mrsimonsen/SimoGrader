import unittest, sys, subprocess
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "yep\nY\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_2(self, stdout):
		correct_out = "my question?\nmy question?\n"
		correct = True
		try:
			result = student.Tools.ask_yn("my question?\n")
			result_out = stdout.getvalue()
			self.assertEqual(result_out, correct_out)
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: ask_yn() function is missing or doesn't return correctly")
		except TypeError:
			self.fail('Message: ask_yn() function has incorrect parameters')
		except NameError:
			self.fail("Message: Tools.py has not been created.")

	inputs = "nope\nN\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_2(self, stdout):
		correct_out = "some question?\nsome question?\n"
		correct = False
		try:
			result = student.Tools.ask_yn("some question?\n")
			result_out = stdout.getvalue()
			self.assertEqual(result_out, correct_out)
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: ask_yn() function is missing or doesn't return correctly")
		except TypeError:
			self.fail('Message: ask_yn() function has incorrect parameters')

	inputs = "-1\nfour\n26\n14\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_3(self, stdout):
		correct_out = "What is the cipher key?\nCipher key must be between 1 and 25 inclusive.\nWhat is the cipher key?\nThat wasn't a number.\nWhat is the cipher key?\nCipher key must be between 1 and 25 inclusive.\nWhat is the cipher key?\n"
		correct = 14
		try:
			result = student.Tools.get_cipher()
			result_out = stdout.getvalue()
			self.assertEqual(result_out, correct_out)
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: get_cipher() function is missing or doesn't return correctly")
		except TypeError:
			self.fail('Message: get_cipher() function has incorrect parameters')

	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_4(self, stdout):
		correct = 'Qcbufohizohwcbg cb twbwgvwbu mcif twboz dfcxsqh! W vcds mci sbxcmsr hvwg qzogg obr vojs o uccr giaasf. Aom hvs Tcfqs ps kwhv mci!\n\nBck tcf gcas dfcufoaawbu eichsg:\n\nRojwr Zshhsfaob: "Vck rwr mci ybck gc aiqv opcih qcadihsfg?"\nUfoqs Vcddsf: "W rwrb\'h, wh kog hvs twfgh cbs."\n\nXsfsam Yswhv: "Xojo wg hc XojoGqfwdh og voa wg hc voaghsf."\n\nCgqof Ucrgcb: "Cbs ct hvs psgh dfcufoaawbu gywzzg mci qob vojs wg ybckwbu kvsb hc kozy okom tcf okvwzs."\n\nZciwg Gfmuzsm: "Kwhvcih fseiwfsasbhg cf rsgwub, dfcufoaawbu wg hvs ofh ct orrwbu piug hc ob sadhm hslh twzs."\n\nPfowb K. Ysfbwuvob: "Rspiuuwbu wg hkwqs og vofr og kfwhwbu hvs qcrs wb hvs twfgh dzoqs. Hvsfstcfs, wt mci kfwhs hvs qcrs og qzsjsfzm og dcggwpzs, mci ofs, pm rstwbwhwcb, bch gaofh sbciuv hc rspiu wh."\n'
		correct_out = ''
		try:
			result = student.Tools.open_file('secret.txt')
			result_out = stdout.getvalue()
			self.assertEqual(result_out, correct_out, "Message: there shouldn't be any output")
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: open_file() function is missing or doesn't return correctly")
		except TypeError:
			self.fail('Message: open_file() function has incorrect parameters')

	@patch('sys.stdout', new_callable = StringIO)
	def test05_part_4(self, stdout):
		correct = None
		correct_out = 'Couldn\'t find "nothing.txt".\n'
		try:
			result = student.Tools.open_file('nothing.txt')
			result_out = stdout.getvalue()
			self.assertEqual(result_out, correct_out)
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: open_file() function is missing or doesn't return correctly")
		except TypeError:
			self.fail('Message: open_file() function has incorrect parameters')

	inputs = "some\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test06_part_5(self, stdout):
		correct_out = "What do you want to call the output file?\n"
		correct = 'some data\n'
		subprocess.run("echo \"some data\" > c.txt", shell=True)
		try:
			student.Tools.write("some data\n")
			result_out = stdout.getvalue()
			self.assertEqual(result_out, correct_out)
		except AttributeError:
			self.fail("Message: write() function is missing or doesn't return correctly")
		except TypeError:
			self.fail('Message: write() function has incorrect parameters')
		result = subprocess.run("diff c.txt some.txt", capture_output=True, text=True, shell=True)
		if result.stdout:
			self.fail("Message: text files were not the same (c.txt, some.txt).")
		elif result.stderr:
			self.fail("Message: 'some.txt' wasn't created exist")
		else:
			subprocess.run("rm some.txt c.txt", shell=True)

	def test07_part_6(self):
		correct = 'cywodrsxq'
		try:
			result = student.Tools.encrypt('something',10)
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: encrypt() function is missing or doesn't return correctly")
		except TypeError:
			self.fail('Message: encrypt() function has incorrect parameters')

	def test08_part_7(self):
		correct = 'something'
		try:
			result = student.Tools.decrypt('cywodrsxq',10)
			self.assertEqual(result, correct)
		except AttributeError:
			self.fail("Message: decrypt() function is missing or doesn't return correctly")
		except TypeError:
			self.fail('Message: decrypt() function has incorrect parameters')

	inputs = "3\ny\nsecret.txt\n0\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test09_part_8(self, stdout):
		self.maxDiff = None
		correct = '''\tWelcome to the Caesar Cipher!
This utility will let you encrypt and decrypt a message from a file you provide.

		MENU
	Option 1: Encrypt Message
	Option 2: Decrypt Message
	Option 3: Letter Distribution Analysis
	Option 0: Exit Program

Choose an option:
Is the message in a file?
What is the name of the file?
a: 19 *******************
b: 36 ************************************
c: 53 *****************************************************
d: 12 ************
e: 02 **
f: 38 **************************************
g: 38 **************************************
h: 45 *********************************************
i: 20 ********************
j: 06 ******
k: 15 ***************
l: 01 *
m: 16 ****************
n: 00
o: 43 *******************************************
p: 09 *********
q: 15 ***************
r: 19 *******************
s: 57 *********************************************************
t: 13 *************
u: 23 ***********************
v: 26 **************************
w: 48 ************************************************
x: 05 *****
y: 06 ******
z: 15 ***************

		MENU
	Option 1: Encrypt Message
	Option 2: Decrypt Message
	Option 3: Letter Distribution Analysis
	Option 0: Exit Program

Choose an option:
'''
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)


if __name__ == "__main__":
	unittest.main(module='tests', failfast=True)