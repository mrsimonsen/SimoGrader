import shelve, csv, os
from make_data import *
from student import Student
from assignment import Assignment
from cleanup import main as clean

def mod_student():
	stu = select_student()
	choice = -1
	while choice != 0 and stu:
		print(stu)
		print("0 - Save/Back to Main Menu")
		print("1 - Change name")
		print("2 - Change github username")
		print("3 - Change class period")
		print("4 - Drop student")
		choice = -1
		while choice not in (0,1,2,3,4):
			choice = validate_num("What would you like to change?")
		if choice == 1:
			print(f"Changing {stu.name} name:")
			stu.name = change("Enter a new name:",stu.name)
		elif choice == 2:
			print(f"Changing {stu.name} username:")
			stu.github = change("Enter a new github username:",stu.github)
		elif choice == 3:
			print(f"Changing {stu.name} period:")
			stu.period = change("Enter a new period for username:",stu.period)
		elif choice == 4:
			print(f"Drop {stu.name}")
			if ask_yn("Are you sure? This CANNOT be undone.") == 'y':
				drop(stu)
				choice = 0
		elif choice == 0:
			d = shelve.open('data.dat')
			students = d['students']
			for i in range(len(students)):
				if students[i].name == stu.name:
					students[i] = stu
					break
			d['students'] = students
			d.close()
			print('Data saved')

def mod_assign():
	stu = select_student()
	choice = None
	if stu:
		index = stu.period-1
		d = shelve.open('data.dat')
		if d['periods'][index] == '1030':
			tags = d['python']
		elif d['periods'][index] == '1400':
			tags = d['java']
		else:
			print(f"{index} isn't set as a programming class")
			choice = 0
		d.close()
	while choice != 0 and stu:
		print(stu)
		print(stu.print_assignments())
		print("0 - Save/Back to Main Menu")
		print("1 - Change a score")
		print("2 - Set as late")
		choice = -1
		while choice not in (0,1,2):
			choice = validate_num("What would you like to do?")
		if choice == 1:
			code, tag = tag_to_index(tags)
			stu.assignments[code].score = change_float("Enter a new score:", stu.assignments[code].score)
		elif choice == 2:
			code = tag_to_index(tags)
			if ask_yn(f"Set {tag} to late?") == 'y':
				stu.assignments[code].set_late()
		elif choice == 0:
			d = shelve.open('data.dat')
			students = d['students']
			for i in range(len(students)):
				if students[i].name == stu.name:
					students[i] = stu
					break
			d['students'] = students
			d.close()
			print('Data saved')

def grade_assignment():
	tag = validate_assign()
	if tag[-1] == 'j':
		grading = '1400'
		ext = '.java'
	elif tag[-1] == 'p':
		grading = '1030'
		ext = '.py'
	else:
		grading = None
		ext = None
	d = shelve.open('data.dat')
	students = d['students']
	d.close()
	for stu in students:
		if stu.course == grading:
			a = stu.assignments[tag]
			if a.score < 5 and a.late:
				print(f"Cloning {stu.name} - late")
				run(['gh','repo','clone',stu.clone(tag),'student'])
				print("Testing...")
				run(['cp',f'Testing/{tag}{ext}', f'student/Tests{ext}'])
				os.chdir('student')
				if ext == '.java':
					a.set_score(run_java())
				elif exit == '.py':
					a.set_score(run_python())
				os.chdir('..')
				print(f"{stu.name}: {tag} - {a.score}/5")
				run(['rm','-rf','student'])
			elif a.score < 10 and not a.late:
				print(f"Cloning {stu.name} - on time")
				run(['gh','repo','clone',stu.clone(tag),'student'])
				print("Testing...")
				run(['cp',f'Testing/{tag}{ext}', f'student/Tests{ext}'])
				os.chdir('student')
				if ext == '.java':
					a.set_score(run_java())
				elif exit == '.py':
					a.set_score(run_python())
				os.chdir('..')
				print(f"{stu.name}: {tag} - {a.score}/10")
				run(['rm','-rf','student'])
			elif (a.score == 10 and not a.late) or (a.score == 5 and a.late):
				print(f"{sut.name} already has completed assignment")
			else:
				print("something strange happened in SimoGrader.grade_assignment()")
			#save the assignment back into the student


def run_python():
	try:
		p = run("python3 Tests.py",shell=True,capture_output=True,text=True)
		score = p.stdout.strip()
	except KeyboardInterrupt:
		print("Student test terminated")
		score = None
	return score
	
	
def main():
	print("Welcome to the Simonsen AutoGrater Data Utility")
	c = 14
	while c != '0':
		print("Main Menu")
		print("0 - Quit")
		print("1 - Grading Menu")
		print("2 - Class Menu")
		print("3 - Student Menu")
		print("4 - Reset Database")
		print("5 - Delete Old Repos")
		c = input("What's your selection?\n")
		
		if c == '0':
			print("Goodbye")
		elif c == '4':
			reset_data()
		elif c == '5':
			clean()
		elif c == '1':
			a = ''
			while a != '0':
				print("Grading Menu")
				print("0 - Return to Main Menu")
				print("1 - Grade an Assignment")
				print("2 - Grade a single Student's Assignment")
				print("3 - Generate Report")
				a = input("What's your selection?\n")

				if a=='0':
					print("Returning to Main Menu")
				elif a == '1':
					grade_assignment()
				elif a == '2':
					pass
					#validate a student
					#validate an assignment for that student
					#grade that student's assignment
						#clone url
						#replace test with mine
						#run test
						#update student assignment score
				elif a == '3':
					pass
					# ask for (python, java, all)
					#create a CSV file w/ header
						#header.append(period, student)
						#for assign in ask:
							#header.append(assign.code)
					#for each student
						#list.append(stu.period, stu.name)
						#for each assignment in stu.assign
							#list.append(stu.assign.score)
						#append data to CSV
				else:
					print("That's not a valid menu option.")
		elif c == '2':
			a = ''
			while a != '0':
				print("Class Menu")
				print("0 - Return to Main Menu")
				print("1 - View Classes")
				print("2 - Set Classes")
				a = input("What's your selection?\n")

				if a == '0':
					print("Returning to Main Menu")
				elif a == '1':
					display_classes()
				elif a == '2':
					set_periods()
				else:
					print("That's not a valid menu option.")
		elif c == '3':
			a = ''
			while a != '0':
				print("Student Menu")
				print("0 - Return to Main Menu")
				print("1 - View a Student")
				print("2 - Import Students")
				print("3 - Modify a Student")
				print("4 - Modify a Student's Assignment")
				a = input ("What's your selection?\n")

				if a == '0':
					print("Returning to Main Menu")
				elif a == '1':
					display_student()
				elif a == '2':
					set_students()
				elif a == '3':
					mod_student()
				elif a == '4':
					mod_assign()
				else:
					print("That's not a valid menu option.")
		else:
			print("That's not a valid menu option.")

if __name__ == "__main__":
	main()
