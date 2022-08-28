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


if __name__ == "__main__":
	unittest.main(module='tests', failfast=True)