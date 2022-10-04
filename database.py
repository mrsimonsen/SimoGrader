import sqlite3
from os import listdir, chdir
from os.path import exists, isdir
from sys import exit

DATABASE_NAME = 'data.sqlite3'

def search_readmes(dir='Example Assignments'):
	'''count the number of steps from the assignment readmes'''
	data = {}
	chdir(dir)
	dirs = [d for d in listdir() if isdir(d)]
	if 'Common Files' in dirs:
		dirs.remove('Common Files')
	for d in dirs:
		chdir(d)
		#check for subdirs
		if not exists('README.md'):
			sub = [s for s in listdir() if isdir(s)]
			for s in sub:
				chdir(s)
				tag, min_commits = get_min_commits(s)
				data[tag] = min_commits
				chdir('..')
		else:
			tag, min_commits = get_min_commits(d)
			data[tag] = min_commits
		chdir('..')
	chdir('..')
	return data

def get_min_commits(d):
	'''extract tag from the given d(irectory)
	count the number of steps in the README
	min_commits is num_steps + 2 (auto generated by GitHub Classroom)'''
	tag = d[:3]
	if tag[0] != 'P': # projects are fine
		try:
			int(tag[0]) #try for regular assignment
			tag = tag[:2]+'p'
		except ValueError:
			tag = 'sol' #and grab the interim assignment
	with open('README.md','r') as f:
		lines = f.readlines()
	steps = []
	for l in lines:
		try:
			int(l[0])#does the line start with a number?
			steps.append(l)
		except ValueError:
			pass#do nothing if it doesn't
	min_commits = len(steps)+2 #add 2 for the 2 commits added by GitHub Classroom
	return tag, min_commits

def execute(query):
	'''connect to the default DATABASE_NAME and try to execute the provided query'''
	connection = sqlite3.connect(DATABASE_NAME)
	cursor = connection.cursor()
	try:
		cursor.execute(query)
		connection.commit()
	except sqlite3.Error as e:
		print(f"Execute Error:\n{e}\n{query}")
		exit()

def read(query):
	'''connect to the default DATABASE_NAME and try to execute the provided query, return the results'''
	connection = sqlite3.connect(DATABASE_NAME)
	cursor = connection.cursor()
	result = None
	try:
		cursor.execute(query)
		result = cursor.fetchall()
	except sqlite3.Error as e:
		print(f"Read Error:\n{e}\n{query}")
		exit()
	return result

def create():
	'''Creates the tables using the default schema for auto-grader.
	Also fills the assignments table by pulling the tags from the test files in the 'Testing' directory
	students: github(text, PK), name (text), period(int)
		github - Student's GitHub username
		name - Student's "last, first (actual)" name
		(university and high school name on record may be different)
		period - What high school class period the student is in
	assignments: tag(text, PK), total(int)
		tag - The prefix tag for the assignment as made in GitHub Classroom
		total - The total points the assignment is worth
		min_commits - The minimum number of commits needed show your works for this assignment
	scores: id(int PK), github(text, FK), tag(text, FK), earned(int)
		id - Primary key used for sorting assignments so the reports display in the order that assignment were given
		github - Foreign key to student's GitHub username
		tag - Foreign key to the assignment's prefix tag
		earned - How many points did the students earn for that assignment
	'''
	create_students_table='''
	CREATE TABLE IF NOT EXISTS students (
		github TEXT PRIMARY KEY,
		name TEXT NOT NULL,
		period INTEGER NOT NULL
	);'''
	execute(create_students_table)
	create_assignments_table='''
	CREATE TABLE IF NOT EXISTS assignments (
		tag TEXT PRIMARY KEY,
		total INTEGER NOT NULL,
		min_commits INTEGER NOT NULL
	);'''
	execute(create_assignments_table)
	create_scores_table='''
	CREATE TABLE IF NOT EXISTS scores (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		tag TEXT NOT NULL REFERENCES assignments(tag),
		github TEXT NOT NULL REFERENCES students(github),
		earned INTEGER
	);'''
	execute(create_scores_table)
	testing = None
	try:
		#assignments are created based on the name of the testing files.
		testing = listdir("Testing")
	except FileNotFoundError as e:
		print(f"Error while trying to load assignments:\n{e}")
	if testing:
		data = search_readmes()
		for file in testing:
			tag = file[:3]
			try:
				#regular assignment start with a number
				int(tag[0])
				points = 10
			except ValueError:
				#projects start with a letter and are worth more
				points = 20
			min_commits = data[tag]
			enter_assignment=f'''
			INSERT INTO assignments (tag, total, min_commits)
			VALUES ('{tag}', {points}, {min_commits});'''
			execute(enter_assignment)

def select_tag():
	'''prompts and validates an assignment tag'''
	ALL = []
	for i in  read('SELECT tag FROM assignments;'):
		ALL.append(i[0])
	tag = ''
	#allow the used to exit without crashing
	while (tag not in ALL) and (tag != 'exit'):
		#ask to display tags if no valid tag is given
		if tag != '' and tag != 'exit':
			if input('Would you like to see the assignment tags?(Y/n)\n').lower() in ('yes','y'):
				print(ALL)
		tag = input("Enter an assignment tag or 'exit' to quit:\n")
	return tag

def select_student(search=''):
	'''prompts and validates a student from the database'''
	github = ''
	while not github:
		if not search:
			search = input("Enter part of a student's name or github or 'exit' to quit:\n")
			if search == 'exit':
				return 'exit'
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
				if c == 'exit':
					return 'exit'
				print("That wasn't a number.")
			except IndexError:
				print("That wasn't a valid option.")
		elif len(results) == 1:
			github = results[0][0]
		else:
			print("No results found. Try again.")
		search = ''
	return github