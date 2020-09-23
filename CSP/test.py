import unittest, datetime
from subprocess import run
from os import getcwd


def catchOutput(inputs=None, seed=''):
	cwd = getcwd()
	p = run(f"python3 {Tests.file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs)
	return p.out

#set up information
#(planet,orbit, gravity)
data = (
	('Mercury',0.241,0.378),
	('Venus',0.615,0.907),
	('Mars',1.88,0.377),
	('Jupiter',11.9,2.36),
	('Saturn',29.4,0.916),
	('Uranus',83.7,0.889),
	('Neptune',163.7,1.12))
Earth_orbit = 365.25
today = datetime.date.today()
file = "solar_trivia.py"
def main():
	score = 0
	total = 1
#	def test_1(self):
	inputs = "Emily\n2015\n08\n17\n40\n"
	d = inputs.split('\n')
	name = d[0]
	
	correct = f"Hi. What's your name?\nHello {name}! I'm going to calculate your stats on the planets in our Solar System.\nFirst I'll need some information, let's start with your birthday.\nWhat year were your born (YYYY)?\nWhat month were you born in (MM)?\nWhat day were you born (DD)?\nOkay, last question. What is your weight?\n"
	result = Tests.catchOutput(inputs)[:len(correct)]
	if result == correct:
		score += 1

	total += 1
#	def test_2(self):
	inputs = "Teresa\n1987\n01\n17\n190\n"
	d = inputs.split('\n')
	name = d[0]
	earth_weight = int(d[4])
	earth_days = (today-datetime.date(int(d[1]),int(d[2]),int(d[3]))).days
	earth_age = round(earth_days/Earth_orbit,1)
	seconds = earth_days*24*60*60
	
	correct = f"Hi. What's your name?\nHello {name}! I'm going to calculate your stats on the planets in our Solar System.\nFirst I'll need some information, let's start with your birthday.\nWhat year were your born (YYYY)?\nWhat month were you born in (MM)?\nWhat day were you born (DD)?\nOkay, last question. What is your weight?\n\nEarth Stats for {name}\nYou've been on this planet for {earth_days} days, which makes you over {seconds} seconds old or {earth_age} years old.\nWith this gravity your weight is {earth_weight} lbs.\n"
	result = Tests.catchOutput(inputs)[:len(correct)]
	if result == correct:
		score += 1
	
	total += 1
#	def test_3(self):
	inputs = "Simonsen\n1988\n03\n01\n275\n"
	d = inputs.split('\n')
	name = d[0]
	earth_weight = int(d[4])
	earth_days = (today-datetime.date(int(d[1]),int(d[2]),int(d[3]))).days
	earth_age = round(earth_days/Earth_orbit,1)
	seconds = earth_days*24*60*60
	
	correct = f"Hi. What's your name?\nHello {name}! I'm going to calculate your stats on the planets in our Solar System.\nFirst I'll need some information, let's start with your birthday.\nWhat year were your born (YYYY)?\nWhat month were you born in (MM)?\nWhat day were you born (DD)?\nOkay, last question. What is your weight?\n\nEarth Stats for {name}\nYou've been on this planet for {earth_days} days, which makes you over {seconds} seconds old or {earth_age} years old.\nWith this gravity your weight is {earth_weight} lbs.\n"
	for i in data:
		planet,orbit,gravity = i
		age = round(earth_age / orbit,1)
		weight = round(earth_weight * gravity,2)
		correct += f"\n{planet} Stats for {name}\nOn this planet you'd be {age} years old.\nWith this gravity you'd weigh {weight} lbs.\n"
	result = Tests.catchOutput(inputs)
	if result == correct:
		score += 1

	return f'{score}/{total}'

if __name__ == "__main__":
	print(main())

