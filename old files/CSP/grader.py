#python grader
import os, csv, shelve, sys
from data_maker import Assignment,Student
from data_maker import main as setup
from subprocess import run

def get_assign():
	f = open('assignment.txt','r')
	assign = f.read()
	return assign

def intro():
	setup()
	print("Python Grader")
	print()
	assign = get_assign()
	data = shelve.open('grading_data')
	assign_obj = data[assign]
	data.close()
	return assign_obj

def gather(a):
	root = os.getcwd()
	#make sure old folder is deleted
	os.mkdir("testing")
	data = shelve.open('grading_data')
	students = data['students']
	for s in students:
		os.chdir('testing')
		os.mkdir(s.github)
		run(['cp',  os.path.join(root,s.github,a.file), os.path.join(root,'testing',s.github,a.file)])
		run(['cp', os.path.join(root,a.test), os.path.join(root,'testing',s.github,'Test.py')])
		os.chdir(root)
	data['students']=students
	data.close()

def grade(a):
	data = shelve.open('grading_data')
	s = data['students']
	data.close()
	root = os.getcwd()
	assign_name = get_assign()
	os.chdir('testing')
	with open(f'{assign_name}report.csv','w',newline='') as f:
		w = csv.writer(f,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		w.writerow(['Period','Student Name','Assignment Name','Points Earned'])
	folders = [f.name for f in os.scandir() if f.is_dir()]
	for f in folders:
		notfound = False
		print(f"Grading: {f}")
		try:
			os.chdir(f)
			p = run("python3 Test.py", shell=True, capture_output=True, text=True)
		except:
			notfound = True
		if e := p.stderr:
			#had an error - auto fail
			print(e)
			points = 0
		elif notfound:
			points = 0
		else:
			score = p.stdout.strip()
			points = string_to_math(score)
		os.chdir('..')
		for student in s:
			if student.github == f:
				student.set_grade(a, points)
	f = open(f'{assign_name}report.csv','a',newline='')
	w = csv.writer(f,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
	s.sort(key=lambda x: x.name)
	for i in s:
		w.writerow([i.period,i.name,assign_name,i.score])
	f.close()
	os.chdir(root)
	data = shelve.open('grading_data')
	data['students'] = s
	data.close()
	os.chdir('..')
	run(['cp', f"Repos/testing/{assign_name}report.csv", f"{assign_name}report.csv"])
	os.chdir(root)

def string_to_math(thing):
	x = thing.split("/")
	score = int(x[0])
	total = int(x[1])
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