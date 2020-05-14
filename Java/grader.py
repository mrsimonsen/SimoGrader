#java grader
import os, csv, datetime, shelve, sys
import SystemCommands as sc
from data_maker import Assignment,Student
from data_maker import main as setup
from subprocess import run

def multi_run(assign_list):
	if assign_list == None:
		assigns = sys.argv[1:]
		assign_list = []
		setup()
		data = shelve.open('grading_data')
		for a in assigns:
			assign_list.append(data[a])
		return assign_list
	elif len(assign_list):
		setup()
		return assign_list
	else:
		return None

def intro():
	setup()
	n=True
	if len(sys.argv)-1:
		assign = sys.argv[1]
		data = shelve.open('grading_data')
		assign_obj = data[assign]
		n = False
	while n:
		print("Java Grader with Python")
		print("This program needs to be ran from the parent directory of the collection of student repos")
		print()
		assign = input("What is the number of the assignment folder?\n")
		try:
			data = shelve.open('grading_data')
			assign_obj = data[assign]
			n = False
		except:
			print("That wasn't a valid assignment number!")
		data.close()
	return assign_obj

def gather(a):
	root = os.getcwd()
	#make sure old folder is deleted
	run(["rm", "-rf", "testing"])
	os.mkdir("testing")
	data = shelve.open('grading_data')
	students = data["students"]
	for s in students:
		os.chdir('testing')
		os.mkdir(s.github)
		if a.folder == "20CaesarCipher":
			run(["cp", os.path.join(root,"test.txt"),os.path.join(s.github,"test.txt")])
			run(["cp", os.path.join(root,"secret.txt"),os.path.join(s.github,"secret.txt")])
			
		for i in a.file:
			run(["cp", os.path.join(root,s.github,a.folder,i), os.path.join(s.github,i)])
			run(["cp", os.path.join(root,a.test), os.path.join(s.github,a.test)])
			os.chdir(os.path.join('..',s.github))
			s.submit = format_date(sc.git_log())
		os.chdir('..')
	data['students']=students
	data.close()

def format_date(raw):
	#format '2019-08-28 14:46:11 -0600'
	#index:  0123456789012345678901234
	year = int(raw[:4])
	month = int(raw[5:7])
	day = int(raw[8:10])
	hour = int(raw[11:13])
	minute = int(raw[14:16])
	second = int(raw[17:19])
	date = datetime.datetime(year, month, day, hour, minute, second)
	return date

def grade(a):
	data = shelve.open('grading_data')
	s = data['students']
	data.close()
	root = os.getcwd()
	os.chdir('testing')
	with open(f'{a.folder[:2]}report.csv','w',newline='') as f:
		w = csv.writer(f,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		w.writerow(['Period','Student Name','assignment name','points earned','is late?'])
	folders = [f.name for f in os.scandir() if f.is_dir()]
	for f in folders:
		print(f"Grading {f}")
		os.chdir(f)
		if sc.compile_java(a.test):
			score = sc.run_java(a.test[:-5])
			points = string_to_math(score)
		else:#didn't compile - auto fail
			print("didn't compile")
			points = 0
		os.chdir("..")
		for student in s:
			if student.github == f:
				student.set_grade(a, points)
	f = open(f'{a.folder[:2]}report.csv','a',newline='')
	w = csv.writer(f,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
	s.sort(key=lambda x:x.name)
	for i in s:
		w.writerow([i.period,i.name,i.assignment.folder,i.score,i.late])
	f.close()
	os.chdir(root)
	os.chdir('..')
	run(["cp", f"Repos/testing/{a.folder[:2]}report.csv", f"{a.folder[:2]}report.csv"])
	os.chdir(root)

def string_to_math(thing):
	x = thing.split("/")
	try:
		if len(x[0])>2:
			score = int(x[0][-2:])
		else:
			score = int(x[0])
		total = int(x[1])
		y = round(score/total * 10,2)
		return y
	except:
		print('error')
		return 0

def main():
	assign_list = None
	if len(sys.argv)-2:
		assign_list = multi_run(assign_list)
		while assign_list:
			assign_obj = assign_list.pop(0)
			print(assign_obj)
			print(f"--Gathering Files {assign_obj.folder}--")	
			gather(assign_obj)
			print(f'--Starting Grading--')
			grade(assign_obj)
			print(f"--{assign_obj.folder} Complete--")
			assign_list = multi_run(assign_list)
	else:
		assign_obj = intro()
		print("--Gathering Files--")
		gather(assign_obj)
		print('--Starting Grading--')
		grade(assign_obj)
	print("--Testing Complete--")

if __name__ == '__main__':
	main()
