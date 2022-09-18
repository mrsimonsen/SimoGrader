import unittest, tests
import student

quit = ('quit','q')
run = ('run','r')
test = ('test','t')
choice = ''

while choice not in quit:
	print("Run - Run students.py program")
	print("Test - Run tests on student.py program")
	print("Quit - exit program")
	choice = input("Choose an option:\n").lower()
	if choice in run:
		print("<----Starting Program---->")
		student.main()
		print("<----Program Complete---->")
	elif choice in test:
		unittest.main(module='tests', failfast=True)
	elif choice in quit:
		print("Goodbye.")
	else:
		print("Invalid selection.")