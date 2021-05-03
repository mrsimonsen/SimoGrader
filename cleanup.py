from github import Github
from dotenv import load_dotenv
from os import environ as env
from subprocess import run
from sys import exit
import datetime
from alive_progress import alive_bar

def validate(prompt):
	not_valid = True
	while not_valid:
		number = input(prompt)
		try:
			number = int(number)
			not_valid = False
		except ValueError as e:
			print(e)
	return number

def get_date():
	year = validate("Year:(####)\n")
	month = validate("Month:(##)\n")
	day = validate("Day:(##)\n")
	return datetime.datetime(year, month, day)

def not_template(name):
	py = ".py"
	java = ".java"
	if name[-3:] != py and name[-5:] != java:
			return True
	return False

def main():
	#get user credentials from .env
	load_dotenv()
	if (token := env.get('TOKEN')) == None:
		print("Edit .env file to have your personal access token.")
		exit()

	#make github object
	g = Github(token)
	print(f"Loaded credentials for {g.get_user().name}")
	#makedir for clone - set name to current date time
	repos = g.get_user().get_repos()
	print("Gathering all repos older than what date?")
	date = get_date()
	print("Gathering Repos...")
	old = []
	total = len(list(repos))
	print("Starting Search..")
	with alive_bar(total, bar='classic', spinner='classic') as bar:
		for r in repos:
			if r.organization == "NUAMES-CS" and not_template(r.name) and r.updated_at < date:
				old.append(r)
			bar()
	for i in old:
		print(i)
	print(f"{len(old)} repos collected")
	if a := (input("Delete?\n").lower() in ('yes','y')):
		for i in old:
			print(f"deleting {i.name}")
			i.delete()
	if not a:
		print("Nothing Deleted.")
	print("Done.")

if __name__ == "__main__":
	main()
