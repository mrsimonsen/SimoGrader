import unittest, subprocess

class Tests(unittest.TestCase):
	file = "right_triangle.py"
	
	def test_1(self):
		inputs = "@\n3\n"
		correct = "Enter a character:\nEnter a triangle height:\n"
		correct += "\n@ \n@ @ \n@ @ @ \n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)
	
	def test_2(self):
		inputs = "%\n5\n"
		correct = "Enter a character:\nEnter a triangle height:\n"
		correct += "\n% \n% % \n% % % \n% % % % \n% % % % % \n"
		result = Tests.catchOutput(inputs)
		self.assertEqual(result, correct)
		
	# setup methods
	@staticmethod
	def catchOutput(inputs=None):
		p = subprocess.run(["python3", Tests.file], capture_output=True, input=inputs, text=True)
		if err:=p.stderr:
			print(err)
		return p.stdout

if __name__ == '__main__':
	unittest.main()