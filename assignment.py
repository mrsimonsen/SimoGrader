import shelve
class Assignment():
	def __init__(self, tag):
		self.tag = tag
		self.score = 0.0
		self.late = False

	def __str__(self):
		rep = f"Assignment {self.tag}\n"
		rep += f"Score: {self.score}/10\n"
		rep += f"Late: {self.late}"
		return rep

	def set_score(self, result):
		if "/" in result:
			points, total = result.split("/")
			score = round(points/total*10,2)
			if self.late:
				#50% late penalty
				if score > 5:
					self.score = 5.0
				else:#was less than 50%
					self.score = score
			else:#not late, full points earned
				self.score = score
		else:#something went wrong, no score
			self.score = 0

	def set_late(self):
		#set late and adjust score
		self.late = True
		if self.score > 5:
			self.score = 5.0
		
