def clean():
	print("Gathering Repos...")
	os.system("gh repo list nuames-cs --json name -L 4444 > temp.json")
	old = []
	d = shelve.open('data.dat')
	tags = d['assignments']
	d.close()
	with open("temp.json") as file:
		repos = json.load(file)
	os.system("rm temp.json")
	print("Filtering Results...")
	for r in repos:
		if r["name"][:3] in tags and r["name"][-3:] != '.py':
			old.append(r['name'])
			print(f"{r['name']} added")
	total = len(old)
	print(f"{total} repos collected")
	if input("Delete?\n").lower() in ('yes','y'):
		c = 0
		print("checking authentication")
		os.system("gh auth refresh -h github.com -s delete_repo")
		for i in old:
			print(f"deleting nuames-cs/{i} ({c}/{total})")
			os.system(f"gh repo delete nuames-cs/{i} --confirm")
	print("Done.")


def select_student(text=None):
	if not text:
		search = input("Enter a part of a student name or '0' to exit:\n")
	else:
		search = text
	if search == '0':
		return None
	d = shelve.open('data.dat')
	students = d['students']
	d.close()
	while search != '0':
		results = []
		for i in students:
			if search.lower() in i.name.lower():
				results.append(i)
		if len(results)>1:
			print("0 - Quit")
			for i in range(len(results)):
				print(f"{i+1} - {results[i].name}")
			n = validate_num("Which student?")-1
			if n >= 0:
				return results[n]
			else:
				return None
		elif len(results)==1:
			return results[0]
		else:
			if search != '0':
				print(f"No students matched \"{search}\"")
				search = input("Enter a part of a student name or '0' to exit:\n")

#function to use as a sorting key in choice 5 of mod_student
def fsort(obj):
	return obj.name

def grade_all():
	stu = select_student()
	if not stu:
		return
	with shelve.open('data.dat') as d:
		students = d['students']
		tags = d['assignments']
	for tag in tags:
		print(f"Grading {tag}")
		grade(stu, tag, False)
	for i in range(len(students)):
		if students[i].name == stu.name:
			students[i] = stu
			break
	with shelve.open('data.dat') as d:
		d['students'] = students
		print("Data saved")
	print(f"{stu.name} Assignments: {stu.github}")
	print(stu.print_assignments())


def report():
	with shelve.open('data.dat') as d:
		students = d['students']
		tags = d['assignments']
	header = ['Period','Name',]
	for tag in tags:
		header.append(tag)
	stuff = [header]
	for stu in students:
		row = [stu.period,stu.name]
		for a in tags:
			s = str(stu.assignments[a].score)
			row.append(s)
		stuff.append(row)
	with open('report.csv','w',newline='') as f:
		w = csv.writer(f, delimiter=',')
		w.writerows(stuff)
	print("Report complete")

def grade_multiple():
	tags = []
	r = ''
	while r != 'done':
		print("Enter assignment tags - type 'done' when finished.")
		r = validate_assign()
		if r != 'done':
			tags.append(r)
			print(tags)
	for tag in tags:
		grade_assignment(tag)
	print(f"Grading and Reporting done for {tags}")
