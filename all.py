from subprocess import run
from data_maker import Assignment, Student
from data_maker import main as setup
import SystemCommands as sc
import shelve, os
from time import sleep

def gather(a, students):
	for s in students:
		os.mkdir(s.github)
		if a.folder == "20CaesarCipher":
			run(["cp", "test.txt", os.path.join(s.github,".")])
			run(["cp", "secret.txt", os.path.join(s.github,".")])
			
		for i in a.file:
			run(["cp", os.path.join("Repos",s.github,a.folder,i), os.path.join(s.github,".")])
		run(["cp", a.test, os.path.join(s.github,".")])

setup()
data = shelve.open('grading_data')
a = data['21']
s = data['students']
data.close()
gather(a,s)

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
		print('0 - error')
