import unittest, sys
from unittest.mock import patch
from io import StringIO

import sqlite3
import database


class Tests(unittest.TestCase):
	def test01_execute(self):
		#create a database
		

