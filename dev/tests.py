from unittest.mock import patch
from io import StringIO
import unittest, sys, os, sqlite3
#import SimoGrader from outside the folder
sys.path.insert(0,f'{os.getcwd()}/../.')
import SimoGrader

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
		correct = [('00p',), ('01p',), ('P00',), ('P01',)]
		#create sample tests for assignment discovery
		os.system('mkdir Testing')
		for i in range(2):
			os.system(f'touch Testing/{i:02}p.py')
			os.system(f'touch Testing/P{i:02}.py')
		SimoGrader.create()
		os.system('rm -rf Testing')
		query = "SELECT tag FROM assignments;"
		result = SimoGrader.read(query)
		self.assertEqual(result, correct)

class Student(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		SimoGrader.create()
	@classmethod
	def tearDownClass(cls):
		os.system('rm data.sqlite3')

	


if __name__ == "__main__":
	unittest.main(failfast=True)

