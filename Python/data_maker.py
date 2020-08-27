#data maker for python
import csv, shelve, datetime
#support classes
class Assignment(object):
	'''an assignment with a file name, due date, and testing file'''

	def __init__(self, afile, due, test):
		self.file = afile
		self.due = due
		self.test = test

	def __str__(self):
		rep = f"{self.file}\n{self.due}\n{self.test}"
		return rep

class Student(object):
	'''a student with name, class period, and github username'''

	def __init__(self, name, period, github):
		self.name = name
		self.period = period
		self.github = github
		self.assignment = Assignment('error',datetime.datetime.today(),'') #default assignment object
		self.score = 0 #default score
		self.late = True #default late status
		self.submit = None #default submisison time

	def __str__(self):
		rep = f"{self.name}, Period {self.period}\n{self.github}\n--Current Assignment--\n{self.assignment.file}\n{self.score} points\nSubmitted:{self.submit}\nLate = {self.late}"
		return rep

	def set_grade(self, assign_obj, score):
		self.assignment = assign_obj
		self.score = score
		if assign_obj.due > self.submit:
			self.late = False

def main():
	#create shelve file, overwrite old file if exists
	data = shelve.open('grading_data','n')

	#assignment details
	assignments = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','1')
	file_names = {'00':'hello_world.py',
	'01':'calculator.py',
	'02':'fortune_cookie.py',
	'03':'coin_flipper.py',
	'04':'GMN2.py',
	'05':'dice_roller.py',
	'06':'counter.py',
	'07':'reverse_message.py',
	'08':'right_triangle.py',
	'09':'WJ2.py',
	'10':'scrambler.py',
	'11':'guess_AI.py',
	'12':'character_creator.py',
	'13':'CC2.py',
	'14':'tv-remote.py',
	'15':'pig-latin.py',
	'1':'hi.py'
	}
	due_dates = {'00':datetime.datetime(2022,8,30,23,59,59),
	'01':datetime.datetime(2020,9,6,23,59,59),
	'02':datetime.datetime(2020,9,13,23,59,59),
	'03':datetime.datetime(2020,9,13,23,59,59),
	'04':datetime.datetime(2020,9,20,23,59,59),
	'05':datetime.datetime(2020,9,27,23,59,59),
	'06':datetime.datetime(2020,9,27,23,59,59),
	'07':datetime.datetime(2020,10,4,23,59,59),
	'08':datetime.datetime(2020,10,4,23,59,59),
	'09':datetime.datetime(2020,10,11,23,59,59),
	'10':datetime.datetime(2020,10,25,23,59,59),
	'11':datetime.datetime(2020,11,1,23,59,59),
	'12':datetime.datetime(2020,11,8,23,59,59),
	'13':datetime.datetime(2020,11,15,23,59,59),
	'14':datetime.datetime(2020,11,29,23,59,59),
	'15':datetime.datetime(2020,12,13,23,59,59),
	'1':datetime.datetime.today()
	}
	tests = {'00': 'test_00.py',
	'01': 'test_01.py',
	'02': 'test_02.py',
	'03': 'test_03.py',
	'04': 'test_04.py',
	'05': 'test_05.py',
	'06': 'test_06.py',
	'07': 'test_07.py',
	'08': 'test_08.py',
	'09': 'test_09.py',
	'10': 'test_10.py',
	'11': 'test_11.py',
	'12': 'test_12.py',
	'13': 'test_13.py',
	'14': 'test_14.py',
	'15': 'test_15.py',
	'1':'test_hi.py'
	}
	for i in assignments:
		data[i]=Assignment(file_names[i],due_dates[i],tests[i])

	#student details
	students = []
	f = open("What's in a Username_ (Responses) - Copy of Form Responses 1.csv",'r',newline='')
		#format = time,first,last,period,git
	raw = csv.reader(f,delimiter=',',quotechar='"')
	for row in raw:
		if row[0] == "Timestamp":
			continue#skip the first row/header
		students.append(Student(f"{row[2]}, {row[1]}",row[3],row[4]))
	f.close()
	data['students'] = students

	#save all the things
	data.close()
