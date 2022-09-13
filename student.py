from database import execute, read
import os

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

def clone(github, tag):
	'''Clone the given student's assignment'''
	os.system(f"gh repo clone nuames-cs/{tag}-{github}")