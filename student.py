

def change_student(github, first_weber=None, first_nuames=None, last=None, period=None):
	found = database.read(database.connect(), f"SELECT * FROM students WHERE github = '{github}'")
	if found:
		old = found[0]
		if first_weber and first_weber != old[1]:
			query = f"UPDATE students SET first_weber = '{first_weber}' WHERE github = '{github}';"
		if 
	else:
		query = f"INSERT INTO students VALUES ('{github}', '{first_weber}', '{first_nuames}', '{last}', {period});"
	database.execute(databse.connect(), query)

def remove_student(github):
	delete_scores =	f"DELETE FROM scores WHERE github = '{github}';"
	database.execute(database.connect(),delete_scores)
	delete_student = f"DELETE FROM students WHERE github = '{github}';"
	database.execute(database.connect(),delete_student)

def change_grade(github, tag, score):
	id = database.read(database.connect(), f"SELECT id FROM scores WHERE github = '{github}' and tag = '{tag}';")
	if id:
		id = id[0][0]
		query = f"UPDATE scores SET earned = {score} WHERE id = {id};"
	else:
		query = f"INSERT INTO scores (github, tag, earned) VALUES ('{github}','{tag}',{score});"
	database.execute(database.connect(), query)

if __name__ == '__main__':
	#change_grade('ssmith2', '12p',0)
	#print(report('ssmith2'))