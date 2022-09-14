from unittest.mock import patch
from io import StringIO
import unittest, sys, os, sqlite3
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
	@classmethod
	def tearDownClass(cls):
		os.system('rm data.sqlite3')
		os.system('rm -r Testing')
	
	def test01_change_student(self):
		'''create a new student'''
		correct = [('skyguy', 'Vader, Darth', 66),('rebel','Organa, Leia', 1),('itsa_mesa','Binks, JarJar',1)]
		SimoGrader.change_student('skyguy','Vader, Darth',66)
		SimoGrader.change_student('rebel','Organa, Leia',1)
		SimoGrader.change_student('itsa_mesa','Binks, JarJar',1)
		query = 'SELECT * FROM students;'
		result = SimoGrader.read(query)
		self.assertEqual(result, correct)

	def test02_change_student(self):
		'''update existing student'''
		correct = [('skyguy', 'Vader, Darth', 66),('rebel','Skywalker, Leia', 2817),('itsa_mesa','Binks, JarJar',1)]
		SimoGrader.change_student('rebel','Skywalker, Leia',2817)
		query = 'SELECT * FROM students;'
		result = SimoGrader.read(query)
		self.assertEqual(result, correct)

	def test03_change_grade(self):
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

	def test04_change_grade(self):
		'''update existing grade'''
		correct = [(1, '00p', 'rebel', 10),(2, '00p', 'skyguy', 7),(3, '00p', 'itsa_mesa', 0),(4, '01p', 'rebel', 10),(5, '01p', 'skyguy', 7),
		(6, '01p', 'itsa_mesa', 2),(7, 'P01', 'rebel', 10),(8, 'P01', 'skyguy', 7),(9, 'P01', 'itsa_mesa', 2),(10, 'st-', 'rebel', 10),
		(11, 'st-', 'skyguy', 10),(12, 'st-', 'itsa_mesa', 2)]
		SimoGrader.change_grade('skyguy','st-',10)
		SimoGrader.change_grade('itsa_mesa','00p',0)
		query = 'SELECT * FROM scores;'
		result = SimoGrader.read(query)
		self.assertEqual(result, correct)

	def test05_remove_student(self):
		'''delete a student'''
		correct = [('rebel', 'Skywalker, Leia', '00p', 10, 10),('skyguy', 'Vader, Darth', '00p', 7, 10),('rebel', 'Skywalker, Leia', '01p', 10, 10),
		('skyguy', 'Vader, Darth', '01p', 7, 10),('rebel', 'Skywalker, Leia', 'P01', 10, 20),('skyguy', 'Vader, Darth', 'P01', 7, 20),
		('rebel', 'Skywalker, Leia', 'st-', 10, 20),('skyguy', 'Vader, Darth', 'st-', 10, 20)]
		SimoGrader.remove_student('itsa_mesa')
		query = '''SELECT scores.github, students.name, scores.tag, earned, assignments.total FROM scores
		INNER JOIN students ON students.github = scores.github
		INNER JOIN assignments ON assignments.tag = scores.tag;'''
		result = SimoGrader.read(query)
		self.assertEqual(result, correct)

	def test06_student_report(self):
		'''generate a student report'''
		correct = '''skyguy - Period: 66
Vader, Darth
--------------------
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
				"\t#prompt for wall height",
				'\theight = float(input("Enter wall height (feet):\\n"))\n',
				"\t#prompt for wall width",
				'\twidth = float(input("Enter wall width (feet):\\n"))\n',
				"\t#calculate wall area",
				'\tarea = height * width\n',
				"\t#display wall area",
				'\tprint(f\"Wall area: {area} square feet\")\n'
			]
			f.writelines(lines)
	
	@classmethod
	def tearDownClass(cls):
		#delete testing data
		os.system('rm data.sqlite3')
		os.system('rm -r Testing')

	#@patch('sys.stdin', StringIO('5.0\n'))
	@patch('sys.stdout',new_callable = StringIO)
	def test01_grade(self, stdout):
		'''test grading regular assignments - full score & simple'''
		correct = [('rebel',10)]
		#students.clone() will fail since these students don't really exist
		#so we're going to mack it's creation
		os.system('mkdir student')
		os.system('mv 00p-rebel.py student/student.py')
		#grade the student
		SimoGrader.grade('rebel','00p')
		result = SimoGrader.read('SELECT github, earned FROM scores WHERE github == "rebel";')
		self.assertEqual(result, correct)

	



if __name__ == "__main__":
	unittest.main(failfast=True)

