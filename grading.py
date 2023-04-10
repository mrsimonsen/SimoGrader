from os import chdir, system, mkdir
from os.path import exists
import json

from database import read
from student import change_grade

GITHUB_ORGANIZATION_NAME = "NUAMES-CS"

def get_text(file):
	with open(file, 'r') as f:
		return f.readlines()

def extract_algorithm(github,tag,now):
	'''extract the comments of the student file as an algorithm text file'''
	#some projects have additional files to check
	text = []
	match tag:
		case 'P10':
			text.append('-----Items.py-----\n')
			text += get_text('Items.py')
			text.append('-----ShoppingCart.py-----\n')
			text += get_text('ShoppingCart.py')
		case 'P11':
			text.append('-----Tools.py-----\n')
			text += get_text('Tools.py')
		case _:
			text = get_text('student.py')
	print(text)
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
	print(github)
	#check if student already complete assignment
	earned = read(f'SELECT earned FROM scores WHERE github == "{github}" AND tag = "{tag}";')
	if earned:
		total = read(f'SELECT total FROM assignments WHERE tag = "{tag}";')
		if earned[0][0]/total[0][0] == 1:
			return "student already complete assignment"
	#clone student repo
	system(f"gh repo clone {GITHUB_ORGANIZATION_NAME}/{tag}-{github} student -- -q 2> out.txt")
	#pipe any errors into a file so that I don't see them
	system('rm out.txt')
	#if the student folder doesn't exist, then it didn't clone
	if not exists('student'):
		return f"Student hasn't accepted the assignment"
	else:
		min_commit = read(f"SELECT min_commits FROM assignments WHERE tag = '{tag}';")[0][0]
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
			system(f"python3 Tests.py {simple} 2> out.txt")
			system('rm out.txt')
			#get the score from the file the test made
			with open('score.txt','r') as f:
				lines = f.readlines()
			score += float(lines[0].strip())
			report = ''.join(lines[1:])
			system("rm score.txt")
			#check for commit count - aka students showing their work
			system("git rev-list --count --all > commits.txt")
			with open("commits.txt",'r') as f:
				commits = int(f.read())
			system("rm commits.txt")
			report += f"Commits: {commits}/{min_commit}\n"
			if min_commit > commits:# they don't have the minimum amount
				score -= 5 #half credit deduction
				if score < 0:
					score = 0 # no negative scores
				report += 'Penalty applied\n'
		except KeyboardInterrupt:
			chdir('..')
			system('rm -rf student')
			return "Student test terminated\n"
		except ValueError as e:
			chdir('..')
			system('rm -rf student')
			return "non-numeric data in score.txt\n"
		except FileNotFoundError:
			chdir('..')
			system('rm -rf student')
			return "Couldn't find score.txt file - student.py probably crashed\n"
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

	print('Loading assignment prefixes...')
	tags = read('SELECT tag FROM assignments;')
	TAGS = ['godot']
	for t in tags:
		TAGS.append(t[0])

	#gather up to 5,000 repo names from the github org
	#~40 assignments with ~100 students, plus ~100 godot (game design)
	print(f'Scraping 5000 repos from {GITHUB_ORGANIZATION_NAME} on GitHub...')
	system(f'gh repo list {GITHUB_ORGANIZATION_NAME} --json name -L 5000 > temp.json')
	remove = []
	with open('temp.json') as f:
		repos = json.load(f)
	system('rm temp.json')
	#filter repos
	print("Filtering repos...")
	for r in repos:
		name = r["name"]
		prefix = name.split('-')[0]
		if prefix in TAGS:
			remove.append(name)
	total = len(remove)
	print(f"{total} repos identified")
	if input("Would you like to view the list before deletion?(Y/n)\n").lower() in ('yes','y'):
		remove.sort()
		with open('repos_to_delete.txt','w') as f:
			for line in remove:
				f.write(line+'\n')
		print("Repos exported to 'repos_to_delete.txt'")
		return
	else:
		print("checking authentication")
		system("gh auth refresh -h github.com -s delete_repo")
		c = 1
		for i in remove:
			print(f"({c:04}/{total}) Deleting: {GITHUB_ORGANIZATION_NAME}/{i}")
			c += 1
			system(f"gh repo delete {GITHUB_ORGANIZATION_NAME}/{i} --confirm")
