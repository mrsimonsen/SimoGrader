import os
from student import change_grade

GITHUB_ORGANIZATION_NAME = "NUAMES-CS"

def extract_algorithm():
	'''extract the comments of the student file as an algorithm text file'''
	with open('student.py','r') as f:
		text = f.readlines()
	algo = []
	for line in text:
		if '#' in line:
			algo.append(line)
	#display the algorithm
	print(''.join(algo))
	score = float(input("Enter a score for the algorithm:\n"))
	return score

def grade(github,tag,simple=True):
	#clone student repo
	os.system(f"gh repo clone {GITHUB_ORGANIZATION_NAME}/{tag}-{github} student -- -q 2> out.txt")
	#pipe any errors into a file so that I don't see them
	os.system('rm out.txt')
	#if the student folder doesn't exist, then it didn't clone
	if not os.path.exists('student'):
		return f"Student hasn't started the assignment"
	else:
		score = 0
		#enter the repo
		os.chdir('student')
		#check if the tag is a project
		if tag[0].isalpha():
			#grade the algorithm
			score += extract_algorithm()
		#run my copy of the tests
		os.system(f"cp ../Testing/{tag}tests.py Tests.py")
		try:
			#run the test
			os.system(f"python3 Tests.py {simple}")
			#get the score from the file the test made
			with open('score.txt','r') as f:
				lines = f.readlines()
			score += float(lines[0].strip())
			report = ''.join(lines[1:])
			os.system("rm score.txt")
		except KeyboardInterrupt:
			return "Student test terminated"
		except ValueError as e:
			return "non-numeric data in score.txt"
		except FileNotFoundError:
			return "Couldn't find score.txt file - student.py probably crashed"
		os.chdir('..')
		os.system('rm -rf student')
		change_grade(github,tag,score)
	return report
