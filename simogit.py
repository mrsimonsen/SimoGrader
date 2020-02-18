from github import Github
from dotenv import load_dotenv
from os import chdir, makedirs, path, listdir, getcwd
from os import environ as env
from subprocess import run
from time import sleep
from sys import exit

status = ""

#get user credentials from .env
load_dotenv()
if (user := env.get('USERNAME')) == None:
		user = input("Enter Username: ")
if (token := env.get('TOKEN')) == None:
		token = input("Enter Password or Token: ")
if (org := env.get('ORG')) == None:
		org = input("Enter Organization name or press enter to skip: ")
if (pre := env.get('PRE')) == None:
		pre = input("Enter repository prefix or press enter to skip: ")
status += f"Loaded credentials for {user}\n"
status += f"Organization: {org}\nRepo prefix: \"{pre}\""
print(status)
#make github object
g = Github(token)
#makedir for clone - set name to current date time
makedirs("Repos")
#cd into folder
chdir("Repos")
#get list of repos 
repos = g.get_user().get_repos()
#clone those starting with prefix
for r in repos:
	if pre in r.name:
		run(["git", "clone", r.ssh_url, r.name[len(pre):]])
		sleep(1)
chdir('..')
run(["clear"])
status+="\nAll repos cloned"
print(status)
print("copying testing files")
if pre == "1030-assignments-":
	loc = "Python"
elif pre == "1400-assignments-":
	loc = "Java"
elif pre == "1410-assignments-":
	loc = "C++"
else:
	print("Location not defined")
	exit()
chdir(loc)
for f in listdir():
	run(["cp", f, path.join('..',"Repos", f)])
status += "\nTest files copied"
run(["clear"])
print(status)
print("\nReady to Grade!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


