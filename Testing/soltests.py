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
t_earth_days = (today - datetime.date(1987, 1, 17)).days
t_earth_age = round(t_earth_days/Earth_orbit,1)
e_earth_days = (today - datetime.date(2015, 8, 17)).days
e_earth_age = round(e_earth_days/Earth_orbit,1)
teresa = f'''Enter Name:
Input birth year (YYYY):
Input birth month (MM):
Input birth day (DD):
Enter weight:

Solar System data for Teresa
Planet |Mercury|Venus  |Earth  |Mars   |Jupiter|Saturn |Uranus |Neptune|
Age    |{round(t_earth_age/data[0][1],1):7}|{round(t_earth_age/data[1][1],1):7}|{round(t_earth_age/data[2][1],1):7}|{round(t_earth_age/data[3][1],1):7}|{round(t_earth_age/data[4][1],1):7}|{round(t_earth_age/data[5][1],1):7}|{round(t_earth_age/data[6][1],1):7}|{round(t_earth_age/data[7][1],1):7}|
Weight |   75.6|  181.4|    200|   75.4|  472.0|  183.2|  177.8|  224.0|
Days   |{int(t_earth_days/data[0][3]):7}|{int(t_earth_days/data[1][3]):7}|{int(t_earth_days/data[2][3]):7}|{int(t_earth_days/data[3][3]):7}|{int(t_earth_days/data[4][3]):7}|{int(t_earth_days/data[5][3]):7}|{int(t_earth_days/data[6][3]):7}|{int(t_earth_days/data[7][3]):7}|
'''
emily = f'''Enter Name:
Input birth year (YYYY):
Input birth month (MM):
Input birth day (DD):
Enter weight:

Solar System data for Emily
Planet |Mercury|Venus  |Earth  |Mars   |Jupiter|Saturn |Uranus |Neptune|
Age    |{round(e_earth_age/data[0][1],1):7}|{round(e_earth_age/data[1][1],1):7}|{round(e_earth_age/data[2][1],1):7}|{round(e_earth_age/data[3][1],1):7}|{round(e_earth_age/data[4][1],1):7}|{round(e_earth_age/data[5][1],1):7}|{round(e_earth_age/data[6][1],1):7}|{round(e_earth_age/data[7][1],1):7}|
Weight |  17.77|  42.63|     47|  17.72| 110.92|  43.05|  41.78|  52.64|
Days   |{int(e_earth_days/data[0][3]):7}|{int(e_earth_days/data[1][3]):7}|{int(e_earth_days/data[2][3]):7}|{int(e_earth_days/data[3][3]):7}|{int(e_earth_days/data[4][3]):7}|{int(e_earth_days/data[5][3]):7}|{int(e_earth_days/data[6][3]):7}|{int(e_earth_days/data[7][3]):7}|
'''

class Tests(unittest.TestCase):
	#to generate correct text
	#$ echo -e "inputs_string" | python3 AK.py > out.txt
	maxDiff = None
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
	return score, report

if __name__ == '__main__':
	if len(sys.argv) > 1:
		score, report = main(sys.argv[1]=='True')
		with open('score.txt','w') as f:
			f.write(str(score))
			f.write('\n'+report)
	else:
		unittest.main(failfast=True)