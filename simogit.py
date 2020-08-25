from github import Github
from dotenv import load_dotenv
from os import chdir, makedirs, path, listdir, getcwd
from os import environ as env
from subprocess import run
from time import sleep
from sys import exit

def verify_pre():
	notValid = True
	p = ('00p','01p','02p','03p','04p','05p','06p','07p','08p','09p','10p','11p','12p','13p','14p','15p')
	j = ('00j','01j','02j','03j','04j','05j','06j','07j','08j','09j','10j','11j','12j','13j','14j','15j','16j','17j','18j','19j','20j','21j')
	while notValid:
		pre = input("Enter repository prefix (assignment code): ")
		if pre in p or pre in j:
			notValid = False
	return pre

status = ""

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
status += f"Loaded credentials for {user}\n"
status += f"Organization: {org}\nRepo prefix: \"{pre}\""
print(status)
#make github object
g = Github(user, password)
#makedir for clone - set name to current date time
makedirs("Repos")
#cd into folder
chdir("Repos")
#get list of repos
repos = g.get_user().get_repos()
#clone those starting with prefix
for r in repos:
	if pre in r.name:
		run(["git", "clone", r.ssh_url, r.name[len(pre)+1:]])
		sleep(1)
chdir('..')
run(["clear"])
status+="\nAll repos cloned"
print(status)
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
status += "\nTest files copied"
run(["clear"])
print(status)
print("\nReady to Grade!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
