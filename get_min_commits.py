from os import system, listdir, chdir
from os.path import exists, isdir

data = {}

def get_min_commits():
	with open('README.md','r') as f:
		lines = f.readlines()
	steps = []
	for l in lines:
		try:
			int(l[0])#does the line start with a number?
			steps.append(l)
		except ValueError:
			pass#do nothing if it doesn't
	return len(steps)+2 #add 2 for the 2 commits added by GitHub Classroom

def extract_readme(d):
	tag = d[:3]
	if tag[0] != 'P':
		tag = tag[:2]+'p'
	data[tag] = get_min_commits()
	
def search_readmes(dir='Example Assignments'):
	chdir(dir)
	dirs = [d for d in listdir() if isdir(d)]
	if 'Common Files' in dirs:
		dirs.remove('Common Files')
	for d in dirs:
		chdir(d)
		#check for subdirs
		if not exists('README.md'):
			sub = [s for s in listdir() if isdir(s)]
			for s in sub:
				chdir(s)
				extract_readme(s)
				chdir('..')
		else:
			extract_readme(d)
		chdir('..')

if __name__ == '__main__':
	search_readmes()
	print(data)