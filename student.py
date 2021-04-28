import shelve
from assignment import Assignment

class Student():
	def __init__(self, name = "Student, Sample", period = 0, github = 'username'):
		self.name = name
		self.period = period
		self.github = github
		self.assignments = []
		self.add_assignments()
	
	def __str__(self):
		rep = f"{self.name}: {self.github}\n"
		d = shelve.open('data.dat')
		course = d['periods'][self.period-1]
		d.close()
		rep += f"{self.period} - {course}\n"
		return rep
	
	def add_assignments(self):
		d = shelve.open('data.dat')
		course = d['periods'][self.period-1]
		tags = []
		if course == '1030':
			tags = d['python']
		elif course == '1400':
			tags = d['java']
		else:
			print(f"Error - {self.period} not set as a programming class")
			print(f"Check entry for {self.name}")
			d.close()
			exit()
		d.close()
		for t in tags:
			self.assignments.append(Assignment(t))

	def clone(self, tag):
		return f"nuames-cs/{tag}-{self.github}"
	
