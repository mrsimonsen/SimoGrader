from unittest.mock import patch
from io import StringIO
import unittest, sys, os
#import modules from outside the folder
sys.path.insert(0,f'{os.getcwd()}/../.')
import database
import sqlite3

class Tests(unittest.TestCase):
	def tearDown(self):
		'''clean up after each test'''
		os.system('rm -f data.sqlite3')
		os.system('rm -rf Testing')

	def test01_write_read(self):
		'''tests the execute() and read() database functions'''
		correct = [(1, 'some data'), (2, 'more data'), (3, 'another')]
		query = "CREATE TABLE test (id INTEGER PRIMARY KEY AUTOINCREMENT, value TEXT);"
		query2 = "INSERT INTO test(value) VALUES ('some data'),('more data'),('another');"
		query3 = "SELECT * FROM test;"
		database.execute(query)
		database.execute(query2)
		result = database.read(query3)
		self.assertEqual(result, correct)

	def test02_schema_creation(self):
		'''tests the create() database function'''
		correct = [('00p',), ('01p',), ('P00',), ('P01',)]
		#create sample tests for assignment discovery
		os.system('mkdir Testing')
		for i in range(2):
			os.system(f'touch Testing/{i:02}p.py')
			os.system(f'touch Testing/P{i:02}.py')
		database.create()
		query = "SELECT tag FROM assignments;"
		result = database.read(query)
		self.assertEqual(result, correct)

if __name__ == "__main__":
	unittest.main(failfast=True)

