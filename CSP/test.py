import unittest, datetime
from subprocess import run
from os import getcwd

# setup methods
def catchOutput(inputs=None, seed=''):
	cwd = getcwd()
	p = run(f"python3 {file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs)
	return p.stdout


def table(earth_age, earth_weight, earth_days):
	rows = ["Planet |","Age    |","Weight |","Days   |"]
	for entry in data:
		planet, orbit, gravity, rotation = entry
		age = round(earth_age / orbit, 1)
		weight = round(earth_weight * gravity, 2)
		days = int(earth_days / rotation)
		rows[0] += f"{planet:7}|"
		rows[1] += f"{age:7}|"
		rows[2] += f"{weight:7}|"
		rows[3] += f"{days:7}|"

	for i in range(len(rows)):
		rows[i] += "\n"
	return rows


def start(name):
	return f"Enter Name:\nInput birth year (YYYY):\nInput birth month (MM):\nInput birth day (DD):\nEnter weight:\n\nSolar System data for {name}\n"


#set up information
Earth_orbit = 365.25
data = (
	('Mercury', 0.241, 0.378, 58.8),
	('Venus', 0.615, 0.907, 244),
	('Earth', 1, 1, 1),
	('Mars', 1.88, 0.377, 1.03),
	('Jupiter', 11.9, 2.36, 0.415),
	('Saturn', 29.4, 0.916, 0.445),
	('Uranus', 83.7, 0.889, 0.720),
	('Neptune', 163.7, 1.12, 0.673)
)
file = "solar_trivia.py"
today = datetime.date.today()

def main():
	total = 80
	score = 0

	#def test_1(self):
	inputs = "Teresa\n1987\n01\n17\n200\n"
	ins = inputs.split('\n')
	n = ins[0]
	correct = start(n)
	result = catchOutput(inputs)[:len(correct)]
	if result == correct:
		score += 24

	#def test_2(self):
	inputs = "Emliy\n2015\n08\n17\n42\n"
	ins = inputs.split('\n')
	n = ins[0]
	w = int(ins[4])
	d = (today-datetime.date(int(ins[1]),int(ins[2]),int(ins[3]))).days
	a = round(d/Earth_orbit,1)

	correct = start(n)
	t = table(a,w,d)
	for i in range(3):
		correct += t[i]

	result = catchOutput(inputs)[:len(correct)]
	if result == correct:
		score += 40

	#Hidden test
	inputs = "Simonsen\n1988\n03\n01\n275\n"
	ins = inputs.split('\n')
	n = ins[0]
	w = int(ins[4])
	d = (today-datetime.date(int(ins[1]),int(ins[2]),int(ins[3]))).days
	a = round(d/Earth_orbit,1)

	correct = start(n)
	t = table(a,w,d)
	for i in t:
		correct += i

	result = catchOutput(inputs)
	if result == correct:
		score += 16

	return f"{score}/{total}"

if __name__ == '__main__':
	print(main())
