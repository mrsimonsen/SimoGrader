import unittest, subprocess
from subprocess import run
from os import getcwd
import guess_AI

class Tests(unittest.TestCase):
	file = "guess_AI.py"
	INTRO = "I am a special mind-reading machine and will guess the number you're thinking of between 1 and 100 in 6 tries or less.\nAfter each guess, tell me if I'm 'high', 'low', or 'correct'.\n"
	
	def test_1(self):
		inputs = "yo\nLOW\n"
		correct = Tests.INTRO
		correct += "For try 1 I guess 50\n"
		correct += "Am I 'high', 'low', or 'correct'?\n"
		correct += "Am I 'high', 'low', or 'correct'?\n"
		result = Tests.catchOutput(inputs, '0')[:len(correct)]
		self.assertEqual(result, correct)
	
	def test_2(self):
		with self.subTest():
			correct = "I knew I could beat you, and in 6 tries too!\nGoodbye."
			result = guess_AI.end(6, 'correct')
			self.assertEqual(result, correct)
		with self.subTest():
			correct = "I ran out of tries! You bested me!\nGoodbye."
			result = guess_AI.end(7, 'correct')
			self.assertEqual(result, correct)
		with self.subTest():
			correct = "I ran out of tries! You bested me!\nGoodbye."
			result = guess_AI.end(3, 'low')
			self.assertEqual(result, correct)
			
	def test_3(self):
		with self.subTest():
			self.assertEqual(guess_AI.high_low(1,100,50,'high',5,True), (1,49,6,True))
		with self.subTest():
			self.assertEqual(guess_AI.high_low(1,100,20,'low',2,True), (21,100,3,True))
		with self.subTest():
			self.assertEqual(guess_AI.high_low(1,100,50,'correct',5,True), (1,100,5,False))
		with self.subTest():
			self.assertEqual(guess_AI.high_low(1,100,50,'low',6,True), (1,100,6,False))
	
		
# setup methods
	@staticmethod
	def catchOutput(inputs=None, seed=''):
		cwd = getcwd()
		p = run(f"python3 {Tests.file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs)
		return p.stdout

if __name__ == '__main__':
	unittest.main()
