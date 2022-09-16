import csv

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
	with open(f'report.csv','w',newline='') as f:
		w = csv.writer(f, delimiter=',')
		w.writerows(stuff)
	print("Report complete")
