#This is the CLI interface

from database import *
from student import *
from grading import *

def display_menu(name, options):
	'''pretty formatting for menus'''
	max = 0
	for i in options:
		max = max if len(i) < max else len(i)
	print(f"{name:^{max}}\n{'-'*9:^{max}}")
	for o in options:
		print(o)
	return input("What is your selection?\n")


def main():
	c = ''
	#check if there is a database
	if not exists('data.sqlite3'):
		print('Class has not been set up (database missing)')
		a = input("Would you like to create the database and import students?(Y/n)\n").lower()
		if a in ('yes','y'):
			print('--Creating database--')
			create()
			import_students()
		else:
			print("SimoGrader can't run without the database.")
			c='0'

	while c != '0':
		#main menu
		options = [
			"'0' to quit the program",
			"'1' - Grading Menu",
			"'2' - Class Menu",
			"'3' - Student Menu",
		]
		c=display_menu('Main Menu', options)
		print()

		#menu selection
		if c == '0':
			print('Goodbye.')
		elif c == '1':
			g = ''
			options = [
				"'0' - Return to Main Menu",
				"'1' - Grade an assignment",
				"'2' - Grade multiple assignments",
				"'3' - Grade a student's assignment",
				"'4' - Grade all of a student's assignments"
			]
			while g != '0':
				g = display_menu('Grading Menu', options)
				if g == '0':
					print('Returning...')
				elif g == '1':
					grade_assignment(select_tag())
				elif g == '2':
					tags = []
					while 'exit' not in tags:
						tags.append(select_tag())
					for tag in tags:
						grade_assignments(tag)
				elif g == '3':
					#grade single student assignment

					#select student
					#select tag
					#grade w/ verbose output
				elif g == '4':
					#grade all student's assignments

					#select student
					#grade all tags
					#display student report
				else:
					print(f"Invalid selection: '{g}'")

		elif c == '2':
			print('class')
		elif c == '3':
			print('student')
		else:
			print(f"Invalid selection: '{c}'")

if __name__ == "__main__":
	main()