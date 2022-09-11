import sqlite3
from os.path import exists
from os import listdir

DATABASE_NAME = 'data.sqlite3'

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
	'''connect to the default DATABASE_NAME and try to execute the provided query and return the results'''
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
	students: github(text, PK), first_weber(text), first_nuames(text), last(text), period(int)
		github - Student's GitHub username
		first_weber - Student's first name on record with Weber State University
		first_nuames - Student's first name on record with NUAMES
		(university and high school name on record may be different)
		last - Student's last name on record
		period - What high school class period the student is in
	assignments: tag(text, PK), total(int)
		tag - The prefix tag for the assignment as made in GitHub Classroom
		total - The total points the assignment is worth
	scores: github(text, FK), tag(text, FK), earned(int), PK(tag,github)
		github - Foreign key to student's GitHub username
		tag - Foreign key to the assignment's prefix tag
		earned - How many points did the students earn for that assignment
	'''
	create_students_table='''
	CREATE TABLE IF NOT EXISTS students (
		github TEXT PRIMARY KEY,
		first_weber TEXT NOT NULL,
		first_nuames TEXT,
		last TEXT NOT NULL,
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
		tag TEXT NOT NULL REFERENCES assignments(tag),
		github TEXT NOT NULL REFERENCES students(github),
		earned INTEGER,
		PRIMARY KEY (tag, github)
	);'''
	execute(create_scores_table)
	testing = None
	try:
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

if __name__ == "__main__":
	create()
	print(read("select tag from assignments;"))
	