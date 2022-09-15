from unittest.mock import patch
from io import StringIO
import unittest, sys, os, sqlite3, csv
#import from outside the folder
sys.path.insert(0,f'{os.getcwd()}/../.')
import SimoGrader

DUMMY_TESTS = ('00p','01p','P01','st-')
def mock_tests():
	'''create sample tests for assignment discovery'''
	os.system('mkdir Testing')
	for i in DUMMY_TESTS:
		os.system(f'touch Testing/{i}.py')

class Database(unittest.TestCase):
	def tearDown(self):
		'''clean up after each test'''
		os.system('rm data.sqlite3')

	def test01_write_read(self):
		'''tests the execute() and read() database functions'''
		correct = [(1, 'some data'), (2, 'more data'), (3, 'another')]
		query = "CREATE TABLE test (id INTEGER PRIMARY KEY AUTOINCREMENT, value TEXT);"
		query2 = "INSERT INTO test(value) VALUES ('some data'),('more data'),('another');"
		query3 = "SELECT * FROM test;"
		SimoGrader.execute(query)
		SimoGrader.execute(query2)
		result = SimoGrader.read(query3)
		self.assertEqual(result, correct)

	def test02_schema_creation(self):
		'''tests the create() database function'''
		correct = [('00p',), ('01p',), ('P01',), ('st-',)]
		mock_tests()
		SimoGrader.create()
		os.system('rm -rf Testing')
		query = "SELECT tag FROM assignments;"
		result = SimoGrader.read(query)
		self.assertEqual(result, correct)

class Student(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		mock_tests()
		SimoGrader.create()
		with open('test_students.csv','w',newline='') as f:
			w = csv.writer(f,delimiter=',')
			w.writerow(('GitHub','Last','Legal','First','Period'))
			w.writerow(('skyguy','Vader','Anakin','Darth',66))
			w.writerow(('rebel','Organa','Leia','Princess',1))
			w.writerow(('itsa_mesa','Binks','JarJar','',1))
	@classmethod
	def tearDownClass(cls):
		os.system('rm data.sqlite3 test_students.csv')
		os.system('rm -r Testing')
	
	def test01_change_student(self):
		'''tests adding a student to the database'''
		SimoGrader.change_student('itsa_mesa','Binks, JarJar ()',1)
		query = 'SELECT * FROM students;'
		correct = [('itsa_mesa','Binks, JarJar ()',1)]
		result = SimoGrader.read(query)
		self.assertEqual(result, correct)

	inputs = 'abc\ntest_students\n'
	@patch('sys.stdin', StringIO(inputs))
	@patch('sys.stdout', new_callable=StringIO)
	def test02_import_students(self,stdout):
		'''create a new student'''
		SimoGrader.import_students()
		with self.subTest('check output'):
			correct = '''Enter the name of the student CSV file or 'exit':
Could not locate file, try again.
Enter the name of the student CSV file or 'exit':
File located
3 student entries found
--Adding students to database, skipping those who already exist--
new student added
new student added
Binks, JarJar () already exists, skipping
Complete: 2 new students added
'''
			result = stdout.getvalue()
			self.assertEqual(result, correct)
		with self.subTest('check database'):
			correct = [
				('itsa_mesa','Binks, JarJar ()',1),
				('skyguy', 'Vader, Anakin (Darth)', 66),
				('rebel','Organa, Leia (Princess)', 1),
			]
			query = 'SELECT * FROM students;'
			result = SimoGrader.read(query)
			self.assertEqual(result, correct)

	def test03_change_student(self):
		'''update existing student'''
		correct = [
				('itsa_mesa','Binks, JarJar ()',1),
				('skyguy', 'Vader, Anakin (Darth)', 66),
				('rebel','Skywalker, Leia ()', 2817),
			]
		SimoGrader.change_student('rebel','Skywalker, Leia ()',2817)
		query = 'SELECT * FROM students;'
		result = SimoGrader.read(query)
		self.assertEqual(result, correct)

	def test04_change_grade(self):
		'''create new grades'''
		correct = [(1, '00p', 'rebel', 10),(2, '00p', 'skyguy', 7),(3, '00p', 'itsa_mesa', 2),(4, '01p', 'rebel', 10),(5, '01p', 'skyguy', 7),
		(6, '01p', 'itsa_mesa', 2),(7, 'P01', 'rebel', 10),(8, 'P01', 'skyguy', 7),(9, 'P01', 'itsa_mesa', 2),(10, 'st-', 'rebel', 10),
		(11, 'st-', 'skyguy', 7),(12, 'st-', 'itsa_mesa', 2)]
		for i in DUMMY_TESTS:
			SimoGrader.change_grade('rebel',i,10)
			SimoGrader.change_grade('skyguy',i,7)
			SimoGrader.change_grade('itsa_mesa',i,2)
		query = 'SELECT * FROM scores;'
		result = SimoGrader.read(query)
		self.assertEqual(result, correct)

	def test05_change_grade(self):
		'''update existing grade'''
		correct = [(1, '00p', 'rebel', 10),(2, '00p', 'skyguy', 7),(3, '00p', 'itsa_mesa', 0),(4, '01p', 'rebel', 10),(5, '01p', 'skyguy', 7),
		(6, '01p', 'itsa_mesa', 2),(7, 'P01', 'rebel', 10),(8, 'P01', 'skyguy', 7),(9, 'P01', 'itsa_mesa', 2),(10, 'st-', 'rebel', 10),
		(11, 'st-', 'skyguy', 10),(12, 'st-', 'itsa_mesa', 2)]
		SimoGrader.change_grade('skyguy','st-',10)
		SimoGrader.change_grade('itsa_mesa','00p',0)
		query = 'SELECT * FROM scores;'
		result = SimoGrader.read(query)
		self.assertEqual(result, correct)

	def test06_remove_student(self):
		'''delete a student'''
		correct = [
			('rebel', 'Skywalker, Leia ()'),
			('skyguy', 'Vader, Anakin (Darth)')
			]
		SimoGrader.remove_student('itsa_mesa')
		query = '''SELECT scores.github, students.name FROM scores
		INNER JOIN students ON students.github = scores.github
		GROUP BY scores.github;'''
		result = SimoGrader.read(query)
		self.assertEqual(result, correct)

	def test07_student_report(self):
		'''generate a student report'''
		correct = '''skyguy - Period: 66
Vader, Anakin (Darth)
----------------------
|Tag|Obtained|	|Tag|Obtained|	|Tag|Obtained|	|Tag|Obtained|	
______________	______________	______________	______________	
|00p|07.00/10|	|01p|07.00/10|	|P01|07.00/20|	|st-|10.00/20|
'''
		result = SimoGrader.student_report('skyguy')
		self.assertEqual(result, correct)


class Grading(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#copy tests
		os.mkdir('Testing')
		os.system('cp ../Testing/00ptests.py Testing/00ptests.py')
		os.system('cp ../Testing/P01tests.py Testing/P01tests.py')
		#create students
		SimoGrader.create()
		SimoGrader.change_student('skyguy', 'Vader, Darth', 6)
		SimoGrader.change_student('rebel','Organa, Leia', 1)
		SimoGrader.change_student('zesa','Binks, JarJar',4)
		#create testing student files
		with open("00p-rebel.py",'w') as f:
			f.write("def main():\n\tprint('Hello World!\\nNUAMES\\n\\tCS')\n")
		with open("00p-skyguy.py",'w') as f:
			f.write("def main():\n\tprint('Hello World!')\n")
		with open("P01-skyguy.py",'w') as f:
			lines = [
				"def main():\n",
				"\tSQFT_PER_GAL = 350.0\n",
				'\theight = float(input("Enter wall height (feet):\\n"))\n',
				'\twidth = float(input("Enter wall width (feet):\\n"))\n',
				'\tarea = height * width\n',
				'\tprint(f\"Wall area: {area} square feet\")\n'
			]
			f.writelines(lines)
		with open("P01-rebel.py",'w') as f:
			lines = [
				"def main():\n",
				"\tSQFT_PER_GAL = 350.0\n",
				"\t#prompt for wall height\n",
				'\theight = float(input("Enter wall height (feet):\\n"))\n',
				"\t#prompt for wall width\n",
				'\twidth = float(input("Enter wall width (feet):\\n"))\n',
				"\t#calculate wall area\n",
				'\tarea = height * width\n',
				"\t#display wall area\n",
				'\tprint(f\"Wall area: {area} square feet\")\n'
			]
			f.writelines(lines)
	
	@classmethod
	def tearDownClass(cls):
		#delete testing data
		os.system('rm data.sqlite3')
		os.system('rm -r Testing')

	def test01_grade_simple(self):
		'''test grading regular assignment - full score & simple'''
		#students.clone() will fail since these students don't really exist
		#so we're going to mock it's creation
		os.system('mkdir student')
		os.system('cp 00p-rebel.py student/student.py')
		#grade the student
		report = SimoGrader.grade('rebel','00p')
		with self.subTest("check database"):
			correct = [('rebel',10)]
			result = SimoGrader.read('SELECT github, earned FROM scores WHERE github == "rebel";')
			self.assertEqual(result, correct)
		with self.subTest("check report"):
			correct = 'Passed: 3/3\nScore: 10\n'
			self.assertEqual(report,correct)

	def test02_grade_verbose(self):
		'''test grading regular assignment - partial points & verbose'''
		#students.clone() will fail since these students don't really exist
		#so we're going to mock it's creation
		os.system('mkdir student')
		os.system('mv 00p-skyguy.py student/student.py')
		#grade the student
		report = SimoGrader.grade('skyguy','00p',False)
		with self.subTest("check database"):
			correct = [('skyguy',3.33)]
			result = SimoGrader.read('SELECT github, earned FROM scores WHERE github == "skyguy";')
			self.assertEqual(result, correct)
		with self.subTest("check report"):
			correct = 'Passed: 1/3\nScore: 3.33\nFailed:\n\tFail: test02_part_2\n\tFail: test03_part_3\n'
			self.assertEqual(report, correct)

	@patch('sys.stdout', new_callable = StringIO)
	@patch('sys.stdin', StringIO('10\n'))
	def test03_grade_algo_simple(self, stdout):
		'''test grading project - half score code & full score algo'''
		#students.clone() will fail since these students don't really exist
		#so we're going to mock it's creation
		os.system('mkdir student')
		os.system('mv P01-rebel.py student/student.py')
		#grade the student
		report = SimoGrader.grade('rebel','P01')
		with self.subTest('check algorithm'):
			correct = '''\t#prompt for wall height
	#prompt for wall width
	#calculate wall area
	#display wall area

Enter a score for the algorithm:
'''
			algo = stdout.getvalue()
			self.assertEqual(algo, correct)
		with self.subTest("check database"):
			correct = [('rebel',15)]
			result = SimoGrader.read('SELECT github, earned FROM scores WHERE github == "rebel" AND tag == "P01";')
			self.assertEqual(result, correct)
		with self.subTest("check report"):
			correct = 'Passed: 2/4\nScore: 5.0\n'
			self.assertEqual(report,correct)

	@patch('sys.stdout', new_callable = StringIO)
	@patch('sys.stdin', StringIO('0.00\n'))
	def test04_grade_algo_verbose(self, stdout):
		'''test grading project - half score code & no score algo, verbose'''
		#students.clone() will fail since these students don't really exist
		#so we're going to mock it's creation
		os.system('mkdir student')
		os.system('mv P01-skyguy.py student/student.py')
		#grade the student
		report = SimoGrader.grade('skyguy','P01',False)
		with self.subTest('check algorithm'):
			correct = '\nEnter a score for the algorithm:\n'
			algo = stdout.getvalue()
			self.assertEqual(algo, correct)
		with self.subTest("check database"):
			correct = [('skyguy',5)]
			result = SimoGrader.read('SELECT github, earned FROM scores WHERE github == "skyguy" AND tag == "P01";')
			self.assertEqual(result, correct)
		with self.subTest("check report"):
			correct = 'Passed: 2/4\nScore: 5.0\nFailed:\n\tFail: test03_part_3\n\tFail: test04_part_4\n'
			self.assertEqual(report,correct)

	def test05_grade_assignment(self):
		'''test grade_assignment'''
		#students.clone() will fail since these students don't really exist
		#so we're going to mock it's creation
		os.system('mkdir student')
		#Leia should be skipped because she already complete the assignment with full points
		#We're going to replace Vader's assignment with Leia's for testing
		os.system('mv 00p-rebel.py student/student.py')
		SimoGrader.grade_assignment('00p')
		correct = [
			('rebel',10),
			('skyguy',10),
		]
		result = SimoGrader.read('SELECT github, earned FROM scores WHERE tag = "00p";')
		self.assertEqual(result, correct)


if __name__ == "__main__":
	unittest.main(failfast=True)

