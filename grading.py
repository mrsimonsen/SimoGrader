from os import chdir, system
from os.path import exists

from student import change_grade
from database import read

GITHUB_ORGANIZATION_NAME = "NUAMES-CS"

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
			score += extract_algorithm()
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

def grade_assignment(tag):
	'''grades all student's given assignment'''
	if tag == 'exit':
		#don't try to grade that
		return
	students = read('SELECT github FROM students;')
	for s in students:
		github = s[0]
		grade(github,tag)

def select_tag():
	'''prompts and validates an assignment tag'''
	ALL = []
	for i in  read('SELECT tag FROM assignments;'):
		ALL.append(i[0])
	tag = ''
	#allow the used to exit without crashing
	while tag not in ALL and tag != 'exit':
		#ask to display tags if no valid tag is given
		if tag != '' and tag != 'exit':
			if input('Would you like to see the assignment tags?(Y/n)\n').lower() in ('yes','y'):
				print(ALL)
		tag = input("Enter an assignment tag or 'exit' to quit:\n")
	return tag

def select_student():
	'''prompts and validates a student from the database'''
	search = ''
	github = ''
	while not github:
		search = input("Enter part of a student's name or github or 'exit' to quit:\n")
		results = read(f"SELECT github, name FROM students WHERE github LIKE '%{search}%' OR name LIKE '%{search}%';")
		if len(results) > 1:
			print('--Results--')
			count = 1
			for git,name in results:
				print(f"{count} - {git}: {name}")
				count += 1
			c = input("Which student?\n")
			try:
				c = int(c)-1
				github = results[c][0]
			except ValueError:
				if c != 'exit':
					print("That wasn't a number.")
				else:
					github = c
			except IndexError:
				print("That wasn't a valid option.")
		elif len(results) == 1:
			github = results[0][1]
		else:
			print("No results found. Try again.")
	return github