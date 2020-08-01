#data maker for python
import csv, shelve, datetime
#support classes
class Assignment(object):
	'''an assignment with a file name, due date, and testing file'''

	def __init__(self, file, due, test):
		self.file = file
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
	assignments = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15')
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
				  '15':'pig-latin.py'
				 }
	due_dates = {'00':datetime.datetime(2019, 9, 1, 23, 59,59),
				 '01':datetime.datetime(2019, 9, 8, 23, 59,59),
				 '02':datetime.datetime(2019,9,15,23,59,59),
				 '03':datetime.datetime(2019,9,15,23,59,59),
				 '04':datetime.datetime(2019,9,22,23,59,59),
				 '05':datetime.datetime(2019,9,29,23,59,59),
				 '06':datetime.datetime(2019,9,29,23,59,59),
				 '07':datetime.datetime(2019,10,6,23,59,59),
				 '08':datetime.datetime(2019,10,6,23,59,59),
				 '09':datetime.datetime(2019,10,13,23,59,59),
				 '10':datetime.datetime(2019,10,27,23,59,59),
				 '11':datetime.datetime(2019,11,3,23,59,59),
				 '12':datetime.datetime(2019,11,10,23,59,59),
				 '13':datetime.datetime(2019,11,17,23,59,59),
				 '14':datetime.datetime(2019,12,1,23,59,59),
				 '15':datetime.datetime(2019,12,15,23,59,59)
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
			}
	for i in assignments:
		data[i]=Assignment(file_names[i],due_dates[i],tests[i])

	#student details
	names = {}
	students = []
	with open('usernames - Form Responses 1.csv','r',newline='') as f:
		#format = time,first,last,period,git
		raw = csv.reader(f,delimiter=',',quotechar='"')
		for row in raw:
			if row[0] == "Timestamp":
				continue#skip the first row/header
			students.append(Student(f"{row[2]}, {row[1]}",row[4],row[3]))
	data['students'] = students

	#save all the things
	data.close()
