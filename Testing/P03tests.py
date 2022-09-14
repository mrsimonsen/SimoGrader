import unittest, sys, random
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "0\n0\n0\n0\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1_default(self, stdout):
		correct = "----Grade Calculator----\nI'll calculate a student's final grade based on the following categories:\nGrade Categories:\n\tHomework: 50%\n\tQuizzes:  20%\n\tMidterm:  10%\n\tFinal:    20%\n\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "0\n0\n0\n0\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_1_extra(self, stdout):
		correct = "----Grade Calculator----\nI'll calculate a student's final grade based on the following categories:\nGrade Categories:\n\tHomework: 10%\n\tQuizzes:  20%\n\tMidterm:  30%\n\tFinal:    40%\n\n"
		student.main(10,20,30,40)
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "95\n60\n88\n85\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_2_default(self, stdout):
		correct = "Enter percent earned from Homework:\nEnter percent earned from Quizzes:\nEnter percent earned from Midterm:\nEnter percent earned from Final:\n"
		student.main()
		result = stdout.getvalue()[178:len(correct)+178]
		self.assertEqual(result, correct)

	inputs = "95\n73\n89\n95\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test04_part_3_A(self, stdout):
		correct = "\nFinal Grade: A (90.0%)\n"
		student.main()
		result = stdout.getvalue()[317:]
		self.assertEqual(result, correct)

	inputs = "85\n70\n82\n95\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test05_part_3_B(self, stdout):
		correct = "\nFinal Grade: B (85.1%)\n"
		student.main(10,20,30,40)
		result = stdout.getvalue()[317:]
		self.assertEqual(result, correct)

	inputs = "65\n70\n80\n95\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test06_part_3_C(self, stdout):
		correct = "\nFinal Grade: C (73.5%)\n"
		student.main(40,20,30,10)
		result = stdout.getvalue()[317:]
		self.assertEqual(result, correct)

	inputs = "65\n70\n80\n65\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test07_part_3_D(self, stdout):
		correct = "\nFinal Grade: D (67.0%)\n"
		student.main(10,10,10,70)
		result = stdout.getvalue()[317:]
		self.assertEqual(result, correct)

	inputs = "5\n30\n80\n65\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test08_part_3_F(self, stdout):
		correct = "\nFinal Grade: F (35.75%)\n"
		student.main(10,80,10,5)
		result = stdout.getvalue()[316:]
		self.assertEqual(result, correct)

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
