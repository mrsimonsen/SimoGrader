import database

def report(github):
	c = database.connect()
	
	student_query = f"SELECT period, last, first_weber, first_nuames FROM students WHERE github = '{github}';"
	period, last, first_weber, first_nuames = database.read(c, student_query)[0]
	
	line1 = f"{github} - Period: {period}\n"
	line2 = f"{last}, {first_weber}" + (f" ({first_nuames})\n" if first_nuames else '\n')
	separator = '-'*len(line1) if len(line1) > len(line2) else '-'*len(line2)
	rep = line1+line2+separator

	assignment_query = f'''
	SELECT scores.tag, earned, assignments.total
	FROM scores
	INNER JOIN assignments ON assignments.tag = scores.tag
	WHERE scores.github = "{github}"
	ORDER BY scores.tag;'''
	result = database.read(c, assignment_query)

	for tag, earned, total in result:
		rep += f"\n{tag} | {earned}/{total}"
	return rep

print(report('ssmith2'))