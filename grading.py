from os import chdir, system, mkdir
from os.path import exists

from database import read
from student import change_grade

GITHUB_ORGANIZATION_NAME = "NUAMES-CS"

def extract_algorithm(github,tag,now):
	'''extract the comments of the student file as an algorithm text file'''
	with open('student.py','r') as f:
		text = f.readlines()
	algo = []
	for line in text:
		if '#' in line:
			algo.append(line)
	if now:
		#display the algorithm
		print(''.join(algo))
		score = float(input("Enter a score for the algorithm:\n"))
	else:
		#save for later
		if not exists(f'../{tag}-Algos'):
			mkdir(f'../{tag}-Algos')
		with open(f'../{tag}-Algos/{github}.txt', 'w') as f:
			f.writelines(algo)
		score = 0
	return score

def grade(github,tag,simple=True,now=False):
	#check if student already complete assignment
	earned = read(f'SELECT earned FROM scores WHERE github == "{github}" AND tag = "{tag}";')
	if (10,) in earned:
		return "student already complete assignment"
	#clone student repo
	system(f"gh repo clone {GITHUB_ORGANIZATION_NAME}/{tag}-{github} student -- -q 2> out.txt")
	#pipe any errors into a file so that I don't see them
	system('rm out.txt')
	#if the student folder doesn't exist, then it didn't clone
	if not exists('student'):
		return f"Student hasn't started the assignment"
	else:
		score = 0
		#enter the repo
		chdir('student')
		#check if the tag is a project
		if tag[0].isalpha():
			#grade the algorithm
			score += extract_algorithm(github,tag,now)
		#run my copy of the tests
		system(f"cp ../Testing/{tag}tests.py Tests.py")
		try:
			#run the test
			system(f"python3 Tests.py {simple}")
			#get the score from the file the test made
			with open('score.txt','r') as f:
				lines = f.readlines()
			score += float(lines[0].strip())
			report = ''.join(lines[1:])
			system("rm score.txt")
		except KeyboardInterrupt:
			return "Student test terminated"
		except ValueError as e:
			return "non-numeric data in score.txt"
		except FileNotFoundError:
			return "Couldn't find score.txt file - student.py probably crashed"
		chdir('..')
		system('rm -rf student')
		change_grade(github,tag,score)
	return report

def grade_assignment(tag,now=False):
	'''grades all student's given assignment'''
	if tag == 'exit':
		#don't try to grade that
		return
	students = read('SELECT github FROM students;')
	for s in students:
		github = s[0]
		print(grade(github,tag,True,now))

def clean():
	'''delete student repos from GitHub, cleaning up the ORG for next year.
	This is NOT reversible.

	If students want to keep their work, they will need to have a local copy.
	Students don't have admin access to their repos and forking is disabled
	by default from GitHub Classroom. This is to minimize visibility of 
	completed assignments for future students, reducing cheating.
	That copy can be added to their personal GitHub accounts if they want.

	This used to speed up the grader since it scanned the ORG for repos, but
	I changed assignment templates and the code so that this is no longer the
	case. I just like the ORG clean.'''

	#get a list of assignment tags
	ALL = 'f'
	#list all repos that have prefix '{tag}-'
	#for each repo
		#delete it