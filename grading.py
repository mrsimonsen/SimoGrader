import os
from student import change_grade

def clone(github, tag):
	'''Clone the given student's assignment
	names the folder "student"'''
	#delete an old student assignment if it already exists
	if os.path.exists('student'):
		os.system('rm -rf student')
	os.system(f"gh repo clone nuames-cs/{tag}-{github} student -- -q")

def extract_algorithm():
	'''extract the comments of the student file as an algorithm text file'''
	with open('student.py','r') as f:
		text = f.readlines()
	algo = []
	for line in text:
		if '#' in line:
			algo.append(line)
	#display the algorithm
	print(''.join(algo))
	score = float(input("Enter a score for the algorithm:\n"))
	return score

def grade(github,tag,simple=True):
	clone(github, tag)
	#if the student folder doesn't exist, then it didn't clone
	if not os.path.exists('student'):
		print(f"Student hasn't started the assignment")
	else:
		#enter the repo
		os.chdir('student')
		#run my copy of the tests
		os.system(f"cp ../Testing/{tag}tests.py Tests.py")
		try:
			#run the test
			os.system(f"python3 Tests.py {simple}")
			#get the score from the file the test made
			with open('score.txt','r') as f:
				score = float(f.read())
			os.system("rm score.txt")
			
			#check if the tag is a project
			if tag[0].isalpha():
				score += extract_algorithm()
		except KeyboardInterrupt:
			print("Student test terminated")
			score = 0
		except ValueError as e:
			print("non-numeric data in score.txt")
			score = 0
		except FileNotFoundError:
			print("couldn't find score.txt file\nstudent file probably crashed")
			score = 0
		os.chdir('..')
		os.system('rm -rf student')
		change_grade(github,tag,score)


	


