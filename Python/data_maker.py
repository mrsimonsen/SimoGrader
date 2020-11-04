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
	assignments = ('00p','01p','02p','03p','04p','05p','06p','07p','08p','09p','10p','11p','12p','13p','14p','15p',)
	file_names = {'00p':'hello_world.py',
	'01p':'calculator.py',
	'02p':'fortune_cookie.py',
	'03p':'coin_flipper.py',
	'04p':'GMN2.py',
	'05p':'dice_roller.py',
	'06p':'counter.py',
	'07p':'reverse_message.py',
	'08p':'right_triangle.py',
	'09p':'WJ2.py',
	'10p':'scrambler.py',
	'11p':'guess_AI.py',
	'12p':'character_creator.py',
	'13p':'CC2.py',
	'14p':'tv_remote.py',
	'15p':'pig_latin.py'
	}
	tests = {'00p': 'test_00.py',
	'01p': 'test_01.py',
	'02p': 'test_02.py',
	'03p': 'test_03.py',
	'04p': 'test_04.py',
	'05p': 'test_05.py',
	'06p': 'test_06.py',
	'07p': 'test_07.py',
	'08p': 'test_08.py',
	'09p': 'test_09.py',
	'10p': 'test_10.py',
	'11p': 'test_11.py',
	'12p': 'test_12.py',
	'13p': 'test_13.py',
	'14p': 'test_14.py',
	'15p': 'test_15.py'
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
