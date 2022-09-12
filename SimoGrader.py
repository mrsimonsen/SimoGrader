import sqlite3
from os.path import exists
from os import listdir

DATABASE_NAME = 'data.sqlite3'

#Database Methods

def execute(query):
	'''connect to the default DATABASE_NAME and try to execute the provided query'''
	connection = sqlite3.connect(DATABASE_NAME)
	cursor = connection.cursor()
	try:
		cursor.execute(query)
		connection.commit()
	except sqlite3.Error as e:
		print(f"Execute Error:\n{e}\n{query}")

def read(query):
	'''connect to the default DATABASE_NAME and try to execute the provided query, return the results'''
	connection = sqlite3.connect(DATABASE_NAME)
	cursor = connection.cursor()
	result = None
	try:
		cursor.execute(query)
		result = cursor.fetchall()
		return result
	except sqlite3.Error as e:
		print(f"Read Error:\n{e}\n{query}")

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
		total INTEGER NOT NULL
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
		for file in testing:
			tag = file[:3]
			try:
				#regular assignment start with a number
				int(tag[0])
				points = 10
			except ValueError:
				#projects start with a letter and are worth more
				points = 20
			enter_assignment=f'''
			INSERT INTO assignments (tag, total)
			VALUES ('{tag}', {points});'''
			execute(enter_assignment)
	#also create game design management
	execute("INSERT INTO assignments (tag, total) VALUES ('godot',50);")


#Student Methods

def change_student(github, name=None, period=None):
	'''Create or change a student's details'''
	found = read(f"SELECT * FROM students WHERE github = '{github}'")
	if found:
		old = found[0]
		if name and name != old[1]:
			query = f"UPDATE students SET name = '{name}' WHERE github = '{github}';"
			execute(query)
		if period and period != old[2]:
			query = f"UPDATE students SET period = {period} WHERE github = '{github}';"
			execute(query)
	else:
		query = f"INSERT INTO students VALUES ('{github}', '{name}', {period});"
		execute(query)

def remove_student(github):
	'''Remove a student from the database'''
	delete_scores =	f"DELETE FROM scores WHERE github = '{github}';"
	execute(delete_scores)
	delete_student = f"DELETE FROM students WHERE github = '{github}';"
	execute(delete_student)

def change_grade(github, tag, score):
	'''Create or change a student's grade'''
	id = read(f"SELECT id FROM scores WHERE github = '{github}' and tag = '{tag}';")
	if id:
		id = id[0][0]
		query = f"UPDATE scores SET earned = {score} WHERE id = {id};"
	else:
		query = f"INSERT INTO scores (github, tag, earned) VALUES ('{github}','{tag}',{score});"
	execute(query)

def student_report(github):
	'''Return a string report of a given student's assignments, displaying 4 per line'''
	student_query = f"SELECT period, name FROM students WHERE github = '{github}';"
	result = read(student_query)

	#extract student data if they exist
	if result:
		period, name = result[0]
	else:
		return f"{github}: not found in database"
	
	#format the header
	line1 = f"{github} - Period: {period}\n"
	line2 = f"{name}\n"
	separator = '-'*len(line1) if len(line1) > len(line2) else '-'*len(line2)
	rep = line1+line2+separator+'\n'

	assignment_query = f'''
	SELECT scores.tag, earned, assignments.total
	FROM scores
	INNER JOIN assignments ON assignments.tag = scores.tag
	WHERE scores.github = "{github}"
	ORDER BY id;'''#score ids autoincrement, sorting displays assignments in the order students did them
	result = read(assignment_query)

	#formatted with 4 assignments per line
	rep += "|Tag|Obtained|\t"*4+"\n"
	rep += "______________\t"*4+"\n"
	count = 0
	for tag, earned, total in result:
		count += 1
		rep += f"|{tag}|{earned:05.2f}/{total}|\t"
		#reset counter after 4 entries
		if count == 4:
			count = 0
			#replace last \t with \n
			rep = rep[:-1]+'\n'
	
	return rep