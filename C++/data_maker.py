import csv, shelve, datetime
#support classes
class Assignment(object):
    '''an assignment with a folder, file name, and due date'''

    def __init__(self,folder,file,due,test):
        self.folder = folder
        self.file = file
        self.due = due
        self.test = test

    def __str__(self):
        rep = f"{self.folder}\\{self.file}\n{self.due}\n{self.test}"
        return rep
class Student(object):
    '''a student with name, weber username, and github username'''

    def __init__(self, name, period, github):
        self.name = name
        self.github = github
        self.period = period
        self.assignment = Assignment('error','',datetime.datetime.today(),'')
        self.score = 0
        self.late = True
        self.submit = None

    def __str__(self):
        rep = f"{self.name}, Period {self.period}\n{self.github}\n--Current Assignment--\n{self.assignment.folder}\\{self.assignment.file}\n{self.score} points\nSubmitted:{self.submit}\nLate = {self.late}"
        return rep

    def set_grade(self, assign_obj, score):
        self.assignment = assign_obj
        self.score = score
        if assign_obj.due > self.submit:
            self.late = False
def main():
    #create shelve file, overwrite old file if exists
    data = shelve.open('grading_data','n')
	
	assignments = {}
	file_names = {}
	folders = {}
	due_dates = {}
	tests = {}
	
	for i in assignments:
        data[i]=Assignment(folders[i],file_names[i],due_dates[i],tests[i])

    #student details
    names = {}
    students = []
    with open('username - Form Responses 1.csv','r',newline='') as f:
        #format = time,first,last,git,weber
        raw = csv.reader(f,delimiter=',',quotechar='"')
        for row in raw:
            if row[1] == "What is your first name?":
                continue#skip the first row/header
            students.append(Student(f"{row[2]}, {row[1]}",int(row[3]),row[4]))
    data['students'] = students
    #save all the things
    data.close()