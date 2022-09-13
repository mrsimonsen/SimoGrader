import unittest, sys
from unittest.mock import patch
from io import StringIO
import student

class Tests(unittest.TestCase):
	inputs = "no\nyes\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test01_part_1(self, stdout):
		correct = "Did you ever hear the tragedy of Darth Plagueis The Wise?\n"
		student.main()
		result = stdout.getvalue()[:len(correct)]
		self.assertEqual(result, correct)

	inputs = "nope\ny\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test02_part_2_single(self, stdout):
		correct = "Did you ever hear the tragedy of Darth Plagueis The Wise?\nI thought not. It’s not a story the Jedi would tell you. It’s a \nSith legend. Darth Plagueis was a Dark Lord of the Sith, so \npowerful and so wise he could use the Force to influence the \nmidichlorians to create life... He had such a knowledge of the dark \nside that he could even keep the ones he cared about from dying. \nThe dark side of the Force is a pathway to many abilities some \nconsider to be unnatural. He became so powerful... the only thing he \nwas afraid of was losing his power, which eventually, of course, he \ndid. Unfortunately, he taught his apprentice everything he knew, \nthen his apprentice killed him in his sleep. Ironic. He could save \nothers from death, but not himself.\nDid you ever hear the tragedy of Darth Plagueis The Wise?\n"
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "yeppers\nstop\nexit\ny\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test03_part_2_multiple(self, stdout):
		self.maxDiff = None
		correct = "Did you ever hear the tragedy of Darth Plagueis The Wise?\nI thought not. It’s not a story the Jedi would tell you. It’s a \nSith legend. Darth Plagueis was a Dark Lord of the Sith, so \npowerful and so wise he could use the Force to influence the \nmidichlorians to create life... He had such a knowledge of the dark \nside that he could even keep the ones he cared about from dying. \nThe dark side of the Force is a pathway to many abilities some \nconsider to be unnatural. He became so powerful... the only thing he \nwas afraid of was losing his power, which eventually, of course, he \ndid. Unfortunately, he taught his apprentice everything he knew, \nthen his apprentice killed him in his sleep. Ironic. He could save \nothers from death, but not himself.\nDid you ever hear the tragedy of Darth Plagueis The Wise?\nI thought not. It’s not a story the Jedi would tell you. It’s a \nSith legend. Darth Plagueis was a Dark Lord of the Sith, so \npowerful and so wise he could use the Force to influence the \nmidichlorians to create life... He had such a knowledge of the dark \nside that he could even keep the ones he cared about from dying. \nThe dark side of the Force is a pathway to many abilities some \nconsider to be unnatural. He became so powerful... the only thing he \nwas afraid of was losing his power, which eventually, of course, he \ndid. Unfortunately, he taught his apprentice everything he knew, \nthen his apprentice killed him in his sleep. Ironic. He could save \nothers from death, but not himself.\nDid you ever hear the tragedy of Darth Plagueis The Wise?\nI thought not. It’s not a story the Jedi would tell you. It’s a \nSith legend. Darth Plagueis was a Dark Lord of the Sith, so \npowerful and so wise he could use the Force to influence the \nmidichlorians to create life... He had such a knowledge of the dark \nside that he could even keep the ones he cared about from dying. \nThe dark side of the Force is a pathway to many abilities some \nconsider to be unnatural. He became so powerful... the only thing he \nwas afraid of was losing his power, which eventually, of course, he \ndid. Unfortunately, he taught his apprentice everything he knew, \nthen his apprentice killed him in his sleep. Ironic. He could save \nothers from death, but not himself.\nDid you ever hear the tragedy of Darth Plagueis The Wise?\n"
		student.main()
		result = stdout.getvalue()
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
	print(f"Passed: {passed}/{total}")
	print(f"Score: {score}")
	if not simple:
		failed = []
		for i in result.failures:
			failed.append(f"Fail: {i[0].id()[15:]}")
		for i in result.errors:
			failed.append(f"Error: {i[0].id()[15:]}")
		print("Failed:")
		for i in failed:
			print(f"	{i}")
	return score

if __name__ == '__main__':
	try:
		simple = sys.argv[1]
	except IndexError:
		simple = False
	score = main(simple)
	with open('score.txt','w') as f:
		f.write(str(score))
