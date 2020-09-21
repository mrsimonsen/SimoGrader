#data maker for python
import csv, shelve
#support classes
class Assignment(object):
	'''an assignment with a file name, due date, and testing file'''

	def __init__(self, afile, test):
		self.file = afile
		self.test = test

	def __str__(self):
		rep = f"{self.file}\n{self.test}"
		return rep

class Student(object):
	'''a student with name, class period, and github username'''

	def __init__(self, name, period, github):
		self.name = name
		self.period = period
		self.github = github
		self.assignment = Assignment('error','') #default assignment object
		self.score = 0 #default score

	def __str__(self):
		rep = f"{self.name}, Period {self.period}\n{self.github}\n--Current Assignment--\n{self.assignment.file}\n{self.score} points\n"
		return rep

	def set_grade(self, assign_obj, score):
		self.assignment = assign_obj
		self.score = score


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
		data[i]=Assignment(file_names[i],tests[i])

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
