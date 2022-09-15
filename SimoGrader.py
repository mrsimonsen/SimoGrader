#This is the CLI interface

from database import *
from student import *
from grading import *

def main():
	c = ''
	#check if there is a database
	if not exists('data.sqlite3'):
		print('Class has not been set up (database missing)')
		a = input("Would you like to create the database and import students?(Y/n)\n").lower()
		if a in ('yes','y'):
			print('--Creating database--')
			create()
			#import students
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
		max = 0
		for i in options:
			max = max if len(i) < max else len(i)
		print(f"{'Main Menu':^{max}}\n{'-'*9:^{max}}")
		for o in options:
			print(o)

		c = input("What is your selection?\n")
		print()

		if c == '0':
			print('Goodbye.')
		elif c == '1':
			print('grading')
		elif c == '2':
			print('class')
		elif c == '3':
			print('student')
		else:
			print(f"Invalid selection: '{c}'")

if __name__ == "__main__":
	main()