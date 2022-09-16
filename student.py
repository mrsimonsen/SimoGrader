from csv import DictReader,writer
from os.path import exists

from database import read, execute

def change_student(github, name, period):
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
	if github == 'exit':
		return
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

def import_students():
	'''imports all student's from CSV into database
	Expected CSV Header: GitHub, Last, Legal, First, Period'''
	#get the name of the csv file from the user
	found = False
	while not found:
		file = input("Enter the name of the student CSV file or 'exit':\n")

		#check that the user enter the file extension
		if file != 'exit':
			if '.csv' not in file:
				file += '.csv'
		
		#try to locate the file
		if file == 'exit':
			return
		elif exists(file):
			found = True
			print('File located')
		else:
			print('Could not locate file, try again.')
	
	#load the data from the file
	students = []
	with open(file,newline='') as f:
		#read the csv as a dictionary, header is the keys
		reader = DictReader(f)
		for r in reader:
			try:
				students.append((r['GitHub'],f"{r['Last']}, {r['Legal']} ({r['First']})",int(r['Period'])))
			except KeyError:
				print("CSV file doesn't have the expected header row:\nGitHub, Last, Legal, First, Period")
				return
	print(f"{len(students)} student entries found")
	print("--Adding students to database, skipping those who already exist--")
	count = 0
	for github, name, period in students:
		if read(f'SELECT github FROM students WHERE github = "{github}"'):
			print(f"{name} already exists, skipping")
		else:
			change_student(github, name, period)
			print('new student added')
			count += 1
	print(f"Complete: {count} new students added")

def csv_report():
	tags = read("SELECT tag FROM assignments;")
	students = read(f"SELECT * FROM students;")
	header = ['Period','Name']
	for t in tags:
		header.append(t[0])
	stuff = [header]
	for github, name, period in students:
		row = [period, name]
		for a in tags:
			s = read(f"SELECT earned FROM scores WHERE github = '{github}' AND tag = '{a[0]}';")
			if s:
				row.append(s[0][0])
			else:
				row.append('-')
		stuff.append(row)
	with open(f'class_report.csv','w',newline='') as f:
		w = csv.writer(f, delimiter=',')
		w.writerows(stuff)
	print("Report complete")