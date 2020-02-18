import os, importlib.util, csv, subprocess, datetime, shelve, glob, sys
import SystemCommands as sc
from data_maker import Assignment,Student
from data_maker import main as setup

def intro():
	setup()
	n=True
	try:
		assign = sys.argv[1]
		data = shelve.open('grading_data')
		assign_obj = data[assign]
		n = False
	except:
		pass
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
	subprocess.run(["rm", "-rf", "testing"])
	os.mkdir("testing")
	data = shelve.open('grading_data')
	students = data['students']
	for s in students:
		os.chdir('testing')
		os.mkdir(s.github)
		if a.folder == "20CaesarCipher":
			subprocess.run(["cp", "..\\test.txt", f"{s.github}\\test.txt"])
		for i in a.file:
			subprocess.run(["cp", os.path.join(root,s.github,a.folder,i), os.path.join(root,'testing',s.github,i)])

			subprocess.run(["cp", os.path.join(root,a.test), os.path.join(root,'testing',s.github,a.test)])
			os.chdir('..')
			os.chdir(s.github)
			s.submit = format_date(sc.git_log())
		os.chdir(root)
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
	root = os.getcwd()
	os.chdir('testing')
	with open('report.csv','w',newline='') as f:
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
	f = open('report.csv','a',newline='')
	w = csv.writer(f,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
	s.sort(key=lambda x:x.name)
	for i in s:
		w.writerow([i.period,i.name,i.assignment.folder,i.score,i.late])
	f.close()
	os.chdir(root)
	data['students'] = s
	data.close()
	os.chdir('..')
	subprocess.run(["cp", "Repos/testing/report.csv", "report.csv"])

def string_to_math(thing):
	if "/" in thing:
		thing = thing[:-1]#rm /n
		if len(thing)%3==0:
			#single digit values
			total = int(thing[-1])
			score = int(thing[0])
		elif len(thing)%5==0:
			#double digit values
			total = int(thing[-2:])
			score = int(thing[:2])
		elif len(thing)%2==0:
			#single digit score with 2 digit total
			total = int(thing[-2:])
			score = int(thing[0])
	else:
		return 0
	return round(score/total * 10,2)

def main():
	assign_obj = intro()
	print("--Gathering Files--")
	gather(assign_obj)
	print('--Starting Grading--')
	grade(assign_obj)
	print("--Testing Complete--")

if __name__ == '__main__':
	main()
