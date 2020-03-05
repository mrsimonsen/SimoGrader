import unittest
from subprocess import run
from os import getcwd
import pig_latin

class Tests(unittest.TestCase):
	file = "pig_latin.py"

	def test_1(self):
		correct = "aeiou"
		result = pig_latin.VOWELS
		self.assertEqual(result, correct)
	
	def test_2(self):
		correct = 'appleway'
		result = pig_latin.way_end('apple')
		self.assertEqual(result, correct)
	
	def test_3(self):
		correct = 'appyhay'
		result = pig_latin.ay_end('happy', 1)
		self.assertEqual(result, correct)
	
	def test_4(self):
		correct = "appyhay 5 applesway"
		result = pig_latin.translate("Happy 5 appLes")
		self.assertEqual(result, correct)

	def test_5_6(self):
		with self.subTest(self):
			inputs = "nothing.txt"
			out = "Welcome to the Pig Latin Translator!\n"
			out += "What is the name of the file:\n"
			out += "Message stored in 'pig.txt'\n"
			correct = (out, '1error')
			result = (Tests.catchOutput(inputs), pig_latin.read('nothing.txt'))
			self.assertEqual(result, correct)
		with self.subTest(self):
			correct = "Some message!\nwith 2 lines!\n"
			pig_latin.write(correct)
			result = pig_latin.read('pig.txt')
			self.assertEqual(result, correct)

	def test_7(self):
		with self.subTest(self):
			correct = "appyhay!"
			result = pig_latin.ay_end("happy!", 1)
			self.assertEqual(result, correct)
		with self.subTest(self):
			correct = "eggway,"
			result = pig_latin.way_end("egg,")
			self.assertEqual(result, correct)
		with self.subTest(self):
			correct = '.,!?'
			result = pig_latin.END
			self.assertEqual(result, correct)

	def test_8(self):
		with self.subTest(self):
			correct = "oolschay?\n"
			result = pig_latin.ay_end("school?\n", 3)
			self.assertEqual(result, correct)
		with self.subTest(self):
			correct = "enigmaway.\n"
			result = pig_latin.way_end("enigma.\n")
			self.assertEqual(result, correct)

# setup methods
	@staticmethod
	def catchOutput(inputs=None, seed=''):
		cwd = getcwd()
		p = run(f"python3 {Tests.file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs)
		return p.stdout

if __name__ == '__main__':
	unittest.main()
