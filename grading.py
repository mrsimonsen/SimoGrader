import os

def clone(github, tag):
	'''Clone the given student's assignment
	names the folder "student"'''
	#delete an old student assignment if it already exists
	if os.path.exists('student'):
		os.system('rm -rf student')
	os.system(f"gh repo clone nuames-cs/{tag}-{github} student -- -q")

def grade(github,tag,simple=True):
	clone(github, tag)
	if not os.path.exists('students'):
		print(f"Student hasn't started the assignment")
	else:
		os.chdir('student')
		os.system(f"cp ../Testing/{tag}tests.py Tests.py")
		try:
			os.system(f"python3 Tests.py {simple}")

