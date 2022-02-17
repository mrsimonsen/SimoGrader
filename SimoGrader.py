import shelve
from sys import exit
from make_data import *

def grading_menu():
	a = ''
	while a != '0':
		print("Grading Menu")
		print("0 - Return to Main Menu")
		print("1 - Grade Multiple Assignments")
		print("2 - Grade an Assignment")
		print("3 - Grade a single Student's Assignment")
		print("4 - Grade all of single Student's Assignments")
		print("5 - Set assignment to late")
		print("6 - Generate Report")
		a = input("What's your selection?\n")

		if a=='0':
			print("Returning to Main Menu")
		elif a == '1':
			grade_multiple()
		elif a == '2':
			grade_assignment()
		elif a == '3':
			grade_student()
		elif a == '4':
			grade_all()
		elif a == '5':
			mark_late()
		elif a == '6':
			report()
		elif a == 'exit':
			exit()
		else:
			print("That's not a valid menu option.")

def class_menu():
	a = ''
	while a != '0':
		print("Class Menu")
		print("0 - Return to Main Menu")
		print("1 - View Classes")
		print("2 - Drop Student")
		print("3 - Add Student")
		print("4 - Import Students")
		a = input("What's your selection?\n")

		if a == '0':
			print("Returning to Main Menu")
		elif a == '1':
			display_classes()
		elif a == '2':
			drop()
		elif a == '3':
			create()
		elif a == '4':
			if ask_yn("\n-------------------------------\nThis will delete current student data, are you sure?") == 'y':
				set_periods()
				set_students()
		elif a == 'exit':
			exit()
		else:
			print("That's not a valid menu option.")

def student_menu():
	a = ''
	while a != '0':
		print("Student Menu")
		print("0 - Return to Main Menu")
		print("1 - View a Student")
		print("2 - Modify a Student")
		print("3 - Modify a Student's Assignment")
		a = input ("What's your selection?\n")

		if a == '0':
			print("Returning to Main Menu")
		elif a == '1':
			display_student()
		elif a == '2':
			mod_student()
		elif a == '3':
			mod_assign()
		elif a == 'exit':
			exit()
		else:
			print("That's not a valid menu option.")

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
		elif c == '1':
			grading_menu()
		elif c == '2':
			class_menu()
		elif c == '3':
			student_menu()
		elif c == '4':
			reset_data()
		elif c == '5':
			clean()
		elif c == 'exit':
			exit()
		else:
			print("That's not a valid menu option.")

if __name__ == "__main__":
	main()
