from github import Github
from dotenv import load_dotenv
from os import chdir, makedirs, path, listdir, getcwd
from os import environ as env
from time import sleep
import sys

def verify_pre():
	notValid = False
	p = ('00p','01p','02p','03p','04p','05p','06p','07p','08p','09p','10p','11p','12p','13p','14p','15p')
	j = ('00j','01j','02j','03j','04j','05j','06j','07j','08j','09j','10j','11j','12j','13j','14j','15j','16j','17j','18j','19j','20j','21j')
	pre = None
	try:
		f = open('assignment.txt','r')
		pre = f.read()
		f.close()
		print(f"Running for repo prefix {pre}")
	except:
		notValid=True

	while notValid:
		pre = input("Enter repository prefix (assignment code): ").lower()
		if pre in p or pre in j or pre == 'csp':
			notValid = False
	f = open('assignment.txt','w')
	f.write(pre)
	f.close
	return pre

def main():
	#get user credentials from .env
	load_dotenv()
	if (token := env.get('TOKEN')) ==None:
		print("Edit .env file to have your personal access token.")
		sys.exit()
	if (pre := env.get('PRE')) == None:
			pre = verify_pre()

	#make github object
	g = Github(token)
	print(f"Loaded credentials for {g.get_user().name}")
	#makedir for clone - set name to current date time
	makedirs("Repos")
	run(['cp','assignment.txt','Repos/assignment.txt'])
	run(['cp',"What's in a Username_ (Responses) - Copy of Form Responses 1.csv",'Repos/.'])
	run(['cp','classes.dat','Repos/.'])
	#cd into folder
	chdir("Repos")
	#get list of repos
	repos = g.get_user().get_repos()
	print(f"Gathering repos with prefix: \"{pre}\"")
	#clone those starting with prefix
	for r in repos:
		if pre in r.name:
			run(["git", "clone", r.ssh_url, r.name[len(pre)+1:]])
			#sleep(2)
	chdir('..')
	print("\nAll repos cloned")
	print("copying testing files")
	if pre[2] == "p":
		loc = "Python"
	elif pre[2] == "j":
		loc = "Java"
	else:
		print("Location not defined")
		exit()
	chdir(loc)
	for f in listdir():
		run(["cp", f, path.join('..',"Repos", f)])
	print("\nTest files copied")

if __name__ == "__main__":
	main()
