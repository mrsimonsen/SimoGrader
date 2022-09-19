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
				"'3' - Grade a student's assignment"
			]
			while g != '0':
				g = display_menu('Grading Menu', options)
				if g == '0':
					print('Returning...')
				elif g == '1':
					tag = select_tag()
					if tag != 'exit':
						#if it is a project, would you like to grade the algo now or later?
						now = tag[0].isalpha() and input("Would you like to grade the algorithms now?(Y/n)\n").lower() in ('yes','y')
					grade_assignment(tag,now)
				elif g == '2':
					tags = []
					while 'exit' not in tags:
						tags.append(select_tag())
					for tag in tags:
						#algos will be stored for later with multiple assignment grading
						grade_assignment(tag)
				elif g == '3' or g.isalpha():
					if g.isalpha():
						github = select_student(g)
					else:
						github = select_student()
					if github != 'exit':
						tag = select_tag()
						if tag != 'exit':
							#show extended report and grade algo now
							print(grade(github, tag, False, True))
							print(student_report(github))
				else:
					print(f"Invalid selection: '{g}'")

		elif c == '2':
			g = ''
			options = [
				"'0' - Return to Main Menu",
				"'1' - Import Students",
				"'2' - Drop a Student",
				"'3' - Reset Database",
				"'4' - Delete old student repos",
			]
			while g != '0':
				g = display_menu('Class Menu', options)
				if g == '0':
					print('Returning...')
				elif g == '1':
					import_students()
				elif g == '2':
					remove_student(select_student())
				elif g == '3':
					if input("---WARNING---\nAll existing data will be lost!\nContinue?(Y/n)?\n").lower() in ('yes','y'):
						system(f"rm {DATABASE_NAME}")
						create()
						print(f"{DATABASE_NAME} reset to default schema.")
						print("Students will need to be imported.")
				elif g == '4':
					print("---WARNING---\nAll student GitHub repos will be deleted!\nDatabase will also be deleted!")
					if input('Continue?(Y/n)?\n').lower() in ('yes','y'):
						clean()
						system(f"rm {DATABASE_NAME}")
						print("Cleaning Complete")
						c = '0' #program should exit, no point in running anymore
				else:
					print(f"Invalid selection: '{g}'")
		elif c == '3':
			g = ''
			options = [
				"'0' - Return to Main Menu",
				"'1' - View a Student Report",
				"'2' - Change a Student's data",
				"'3' - Generate Class Report CSV",
			]
			while g != '0':
				g = display_menu('Student Menu', options)
				if g == '0':
					print('Returning...')
				elif g == '1' or g.isalpha():
					if g.isalpha():
						github = select_student(g)
					else:
						github = select_student()
					if github != 'exit':
						print(student_report(github))
				elif g == '2':
					github = select_student()
					if github != 'exit':
						name = input("Enter new name 'Last, Legal (First)' or press 'Enter' to skip\n")
						valid = False
						while not valid:
							try:
								period = input("Enter new class period or press 'Enter' to skip\n")
								period = int(period)
								if period in range(1,9):
									valid = True
							except ValueError:
								if period:
									print("That wasn't a number.")
								else:
									valid = True
						change_student(github,name,period)
				elif g == '3':
					csv_report()
				else:
					print(f"Invalid selection: '{g}'")
		else:
			print(f"Invalid selection: '{c}'")

if __name__ == "__main__":
	main()