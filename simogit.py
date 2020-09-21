from github import Github
from dotenv import load_dotenv
from os import chdir, makedirs, path, listdir, getcwd
from os import environ as env
from subprocess import run
from time import sleep
from sys import exit
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
		pre = input("Enter repository prefix (assignment code): ")
		if pre in p or pre in j:
			notValid = False
	f = open('assignment.txt','w')
	f.write(pre[:2])
	f.close
	return pre

def main():
	#get user credentials from .env
	load_dotenv()
	if (user := env.get('USERNAME')) == None:
			user = input("Enter Username: ")
	if (password := env.get('PASSWORD')) == None:
			password = input("Enter Password:")
	if (org := env.get('ORG')) == None:
			org = input("Enter Organization name or press enter to skip: ")
	if (pre := env.get('PRE')) == None:
			pre = verify_pre()

	print(f"Loaded credentials for {user}\nOrganization: {org}\nRepo prefix: \"{pre}\"")
	#make github object
	g = Github(user, password)
	#makedir for clone - set name to current date time
	makedirs("Repos")
	run(['cp','assignment.txt','Repos/assignment.txt'])
	#cd into folder
	chdir("Repos")
	#get list of repos
	repos = g.get_user().get_repos()
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
