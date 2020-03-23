from grader import gather
from subprocess import run
from data_maker import Assignment, Student
from data_maker import main as setup
import SystemCommands as sc
import shelve, os


setup()
data = shelve.open('grading_data')
a = data['14']
s = data['students']
data.close()
folders = [f.name for f in os.scandir() if f.is_dir()]
for f in folders:
	not_found = True
	for i in s:
		if i.github == f:
			print(f"Gradign {i.name}")
			#print(i.github)
			not_found = False
	if not_found:
		continue
	try:
		os.chdir(f)
		if sc.compile_java(a.test):
			print(sc.run_java(a.test[:-5]))
		else:
			print("didn't compile")
		os.chdir('..')
	except:
		print('0')