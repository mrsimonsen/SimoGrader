import shelve
from make_data import *



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
					grade_student()
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

