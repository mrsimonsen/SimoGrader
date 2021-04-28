import shelve

class Student():
	def __init__(self, name = "Student, Sample", period = 0, github = 'username'):
		self.name = name
		self.period = period
		self.github = github
		self.assignments = []
	
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
		d.close()
		if course == '1030':
			for tag in d['python']:
				self.assignments.append(Assignment(tag))
		elif course == '1400':
			for tag in d['java']:
				self.assignments.append(Assignment(tag))
		else:
			print(f"Error - {self.period} not set as a programming class")
			print(f"Check entry for {self.name}")
			exit()

	def clone(self, tag):
		return f"nuames-cs/{tag}-{self.github}"
	
