import unittest, sys, subprocess
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	def test01_part_1(self):
		correct = "best friend forever I don't know just kidding too much information talk to you later"
		subprocess.run(f"echo \"{correct}\" > text.txt", shell=True)
		subprocess.run("echo \"BFF IDK JK TMI TTYL\" > message.txt", shell = True)
		student.main()
		result = subprocess.run("diff expanded.txt text.txt", capture_output=True, text=True, shell=True)
		if result.stdout:
			self.fail("Message: text files were not the same.")
		elif result.stderr:
			self.fail("Message: 'expanded.txt' doesn't exist")
		else:
			subprocess.run("rm text.txt", shell=True)

	def test02_part_1(self):
		correct = "I don't know how that happened. too much information.\nI'll fix it. just kidding, you know I don't know how.\nYour bff, my best friend forever, and her best friend forever are all there. talk to you later"
		subprocess.run(f"echo \"{correct}\" > text.txt", shell=True)
		subprocess.run("echo \"IDK how that happened. TMI.\nI'll fix it. JK, you know IDK how.\nYour bff, my BFF, and her BFF are all there. TTYL\" > message.txt", shell = True)
		student.main()
		result = subprocess.run("diff expanded.txt text.txt", capture_output=True, text=True, shell=True)
		if result.stdout:
			self.fail("Message: text files were not the same.")
		elif result.stderr:
			self.fail("Message: 'expanded.txt' doesn't exist")
		else:
			subprocess.run("rm text.txt", shell=True)


if __name__ == "__main__":
	unittest.main(module='tests', failfast=True)