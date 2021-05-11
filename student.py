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

	@property
	def course(self):
		d = shelve.open('data.dat')
		p = d['periods']
		d.close()
		return p[self.period - 1]

	
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
	
	def print_assignments(self):
		rep = "|Tag|Score|Late?|\t|Tag|Score|Late?|\n"
		rep +="________________\t________________\n"
		odd = len(self.assignments)%2
		if odd:
			length = len(self.assignments)-1
		else:
			length = len(self.assignments)
		for i in range(0,length,2):
			a1 = self.assignments[i]
			a2 = self.assignments[i+1]
			rep += f"|{a1.tag}|{a1.score:>5}|{str(a1.late):>5}|\t|{a2.tag}|{a2.score:>5}|{str(a2.late):>5}|\n"
		if odd:
			a = self.assignments[-1]
			rep += f"|{a.tag}|{a.score>5}|{str(a.late):>5}|"
		return rep
