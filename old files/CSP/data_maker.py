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
	file_name = 'solar_trivia.py'
	test = 'test.py'
	
	data['CSP'] = Assignment(file_name, test)

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
