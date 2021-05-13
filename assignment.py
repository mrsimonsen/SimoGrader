import shelve
class Assignment():
	def __init__(self, tag):
		self.tag = tag
		self.late = False
		self._score = 0.0

	def __str__(self):
		rep = f"Assignment {self.tag}\n"
		rep += f"Score: {self.score}/10\n"
		rep += f"Late: {self.late}"
		return rep

	@property
	def score(self):
		return self._score
	@score.setter
	def score(self, new):
		if self.late and new > 5:
			self._score = 5.0
		else:
			self._score = new

	def set_score(self, result):
		if result:
			points, total = result.split("/")
			score = round(int(points)/int(total)*10,2)
		else:#something went wrong, no score
			score = 0
		self.score = score

	def set_late(self):
		#set late and adjust score
		self.late = not self.late
		if self.score > 5:
			self.score = 5.0
		
