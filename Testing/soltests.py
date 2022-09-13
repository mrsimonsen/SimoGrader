import unittest, datetime, sys
from unittest.mock import patch
from io import StringIO
import student

#set up information
Earth_orbit = 365.25
data = (
	('Mercury', 0.241, 0.378, 58.8),
	('Venus', 0.615, 0.907, 244),
	('Earth', 1, 1, 1),
	('Mars', 1.88, 0.377, 1.03),
	('Jupiter', 11.9, 2.36, 0.415),
	('Saturn', 29.4, 0.916, 0.445),
	('Uranus', 83.7, 0.889, 0.720),
	('Neptune', 163.7, 1.12, 0.673)
)
today = datetime.date.today()
teresa = '''Enter Name:
Input birth year (YYYY):
Input birth month (MM):
Input birth day (DD):
Enter weight:

Solar System data for Teresa
Planet |Mercury|Venus  |Earth  |Mars   |Jupiter|Saturn |Uranus |Neptune|
Age    |  147.3|   57.7|   35.5|   18.9|    3.0|    1.2|    0.4|    0.2|
Weight |   75.6|  181.4|    200|   75.4|  472.0|  183.2|  177.8|  224.0|
Days   |    220|     53|  12961|  12583|  31231|  29125|  18001|  19258|
'''
emily = '''Enter Name:
Input birth year (YYYY):
Input birth month (MM):
Input birth day (DD):
Enter weight:

Solar System data for Emily
Planet |Mercury|Venus  |Earth  |Mars   |Jupiter|Saturn |Uranus |Neptune|
Age    |   28.6|   11.2|    6.9|    3.7|    0.6|    0.2|    0.1|    0.0|
Weight |  17.77|  42.63|     47|  17.72| 110.92|  43.05|  41.78|  52.64|
Days   |     42|     10|   2522|   2448|   6077|   5667|   3502|   3747|
'''

class Tests(unittest.TestCase):
	#to generate correct text
	#$ echo -e "inputs_string" | python3 AK.py > out.txt
	
	inputs = "Teresa\n1987\n01\n17\n200\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test_1(self, stdout):
		correct = teresa
		student.main()
		result = stdout.getvalue()
		self.assertEqual(result, correct)

	inputs = "Emily\n2015\n08\n17\n47\n"
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable = StringIO)
	def test_2(self, stdout):
		correct = emily
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
		simple = bool(sys.argv[1])
	score = main(simple)
	with open('score.txt','w') as f:
		f.write(str(score))
