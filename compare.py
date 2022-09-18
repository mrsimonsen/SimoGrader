import csv
webers = []
with open('weber.csv',newline='') as f:
	r = csv.reader(f,delimiter=',')
	for row in r:
		if "Student" in row[0]:
			continue
		name, sections, github = row
		sections = sections.replace(' ',',')
		period = sections[0]
		try:
			int(period)
		except ValueError:
			continue
		if github == '0':
			webers.append((name,period))
print(f"{len(webers)} missing github")
for i in webers:
	print(i)


