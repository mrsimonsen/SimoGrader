import shelve, csv
from student import Student
from assignment import Assignment

def reset_data():
	d = shelve.open('data.dat')
	#list of 1030 assignment prefixes
	d['python'] = ('00p','01p','02p','03p','04p','05p','06p','07p','08p','09p','10p','11p','12p','13p','14p','15p')
	#list of 1400 assignment prefixes
	d['java'] = ('00j','01j','02j','03j','04j','05j','06j','07j','08j','09j','10j','11j','12j','13j','14j','15j','16j','17j','18j','19j','20j','21j')
	#list of course periods
	periods = []
	for i in range(8):
		periods.append('empty')
	d['periods'] = periods
	d['students'] = []
	d.close()

def validate_num(question):
	ok = False
	while not ok:
		try:
			number = int(input(f"{question}\n"))
			ok = True
		except ValueError:
			print("That wasn't a number")
	return number

def ask_yn(question):
	r = ''
	while r not in ('y','n'):
		r = input(f"{question} (Y/n)\n").lower()
	return r

def set_periods():
	r = 'n'
	d = shelve.open('data.dat')
	periods = d['periods']
	#while not correct
	while r == 'n':
		n = validate_num("How many 1030 sections this semester?")
		for i in range(n):
			x = validate_num(f"Enter class period for 1030 section number {i+1}:")
			periods[x-1] = '1030'
		n = validate_num("How many 1400 sections this semester?")
		for i in range(n):
			x = validate_num(f"Enter class period for 1400 section number {i+1}:")
			periods[x-1] = '1400'
		print(f"Periods: {periods}")
		r = ask_yn("Is this correct?")
	d['periods'] = periods
	d.close()
	print("Course periods have been saved")

def display_classes():
	with shelve.open('data.dat') as f:
		periods = f['periods']
		p = []
		j = []
		for i in range(len(periods)):
			if periods[i] == '1030':
				p.append(i+1)
			elif periods[i] == '1400':
				j.append(i+1)
		print(f"{len(p)} Python classes, {len(j)} Java classes")
		print(f"\tPython periods: {p}")
		print(f"\tJava periods: {j}")

def set_students():
	students = []
	try:
		f = open("What's in a Username_ (Responses) - Copy of Form Responses 1.csv",'r',newline='')
		print("Loading students...")
		#format: time, first, last, period, github
		raw = csv.reader(f, delimiter= ',', quotechar = '"')
		for row in raw:
			if row[0] == "Timestamp":
				continue #skip the header
			students.append(Student(f"{row[2]}, {row[1]}", int(row[3]), row[4]))
		f.close()
		d = shelve.open('data.dat')
		d['students'] = students
		d.close()
		print(f"{len(students)} loaded")
	except FileNotFoundError as e:
		print(e)
		print("Exiting program -- goodbye.")
		exit()

def display_student():
	done = False
	d = shelve.open('data.dat')
	students = d['students']
	d.close()
	while not done:
		search = input("Enter a part of a student name:\n")
		results = []
		for i in students:
			if search in i.name.lower():
				results.append(i)
		if len(results):
			for i in range(len(results)):
				print(f"{i+1} - {results[i].name}")
			choice = results[validate_num("Which student?")-1]
			print(f"{choice.name} Assignments")
			for i in choice.assignments:
				print(i)
		else:
			print("No students matched \"{search}\"")
		if ask_yn("Go back to main menu?") == 'y':
			done = True
	
def main():
	print("Welcome to the Simonsen AutoGrater Data Utility")
	c = 14
	while c != '0':
		print("0 - Quit")
		print("1 - Reset Data")
		print("2 - View Classes")
		print("3 - Set Classes")
		print("4 - Set All Students")
		print("5 - View a Student Assignment")
		print("6 - Modify a Student")
		print("7 - Modify a Student's Assignment")
		c = input("What's your selection?\n")

		if c =='0':
			print("Goodbye")
		elif c == '1':
			reset_data()
		elif c == '2':
			display_classes()
		elif c == '3':
			set_periods()
		elif c == '4':
			set_students()
		elif c == '5':
			display_student()
		else:
			print("That's not a valid menu option.")

if __name__ == "__main__":
	main()

