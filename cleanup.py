from github import Github
from dotenv import load_dotenv
from os import environ as env
from subprocess import run
from sys import exit
import datetime

java = ('00j', '01j', '02j', '03j', '04j', '05j', '06j', '07j', '08j', '09j', '10j', '11j', '12j', '13j', '14j', '15j', '16j', '17j', '18j', '19j', '20j', '21j')
python = ('00p', '01p', '02p', '03p', '04p', '05p', '06p', '07p', '08p', '09p', '10p', '11p', '12p', '13p', '14p', '15p')

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
	year = validate("Year:\n")
	month = validate("Month:\n")
	day = validate("Day:\n")
	return datetime.datetime(year, month, day)


def main():
	#get user credentials from .env
	load_dotenv()
	if (token := env.get('TOKEN')) ==None:
		print("Edit .env file to have your personal access token.")
		exit()

	#make github object
	g = Github(token)
	print(f"Loaded credentials for {g.get_user().name}")
	#makedir for clone - set name to current date time
	repos = g.get_user().get_repos()
	print("Gathering all repos older than what date?")
	date = get_date()
	old = []
	for r in repos:
		if r.updated_at < date and (r.name[:3] in java or r.name[:3] in python):
			old.append(r)
			print(r)
	print(f"{len(old)} repos collected")
	if input("Delete?").lower() in ('yes','y'):
		for i in old:
			print(f"deleting {i.name}")
			i.delete()

if __name__ == "__main__":
	main()
	print("Done.")
