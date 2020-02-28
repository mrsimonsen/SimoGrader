#Mr. Simonsen
#14

#leave this code or testing won't work
import random, sys
if len(sys.argv)-1:
	random.seed(int(sys.argv[1]))
#########################################################

class Critter():
	"""A virtual pet"""
	def __init__(self, name):
		self.name = name
		self.hunger = random.randrange(10)
		self.boredom = random.randrange(10)

	def __str__(self):
		rep = "Critter Object\n"
		rep += f"Name: {self.name}\n"
		rep += f"Hunger: {self.hunger}\n"
		rep += f"Boredom: {self.boredom}\n"
		rep += f"Mood: {self.mood}"
		return rep

	def __pass_time(self):
		self.hunger += 1
		self.boredom += 1

	@property
	def mood(self):
		unhappiness = self.hunger + self.boredom
		if unhappiness < 5:
			m = "happy"
		elif 5 <= unhappiness <= 10:
			m = "okay"
		elif 11 <= unhappiness <= 15:
			m = "frustrated"
		else:
			m = "mad"
		return m

	def talk(self):
		rep = f"I'm {self.name} and I feel {self.mood} now.\n"
		self.__pass_time()
		return rep

	def eat(self, food = 4):
		self.hunger -= food
		if self.hunger < 0:
			self.hunger = 0
		self.__pass_time()
		return "Brruppp. Thank you."

	def play(self, fun = 4):
		self.boredom -= fun
		if self.boredom < 0:
			self.boredom = 0
		self.__pass_time()
		return "Wheee!"

def main():
	crit_name = input("What do you want to name your critter?\n")
	crit = Critter(crit_name)

	choice = None
	while choice != "0":
		print \
		("""
Critter Caretaker

0 - Quit
1 - Listen to your critter
2 - Feed your critter
3 - Play with your critter""")

		choice = input("Choice:\n")

		# exit
		if choice == "0":
			print("Goodbye.")

		# listen to your critter
		elif choice == "1":
			print(crit.talk())

		# feed your critter
		elif choice == "2":
			food =int(input("How much food do you want to feed your critter?\n"))
			print(crit.eat(food))

		# play with your critter
		elif choice == "3":
			fun =int(input("How much fun do you and your cirtter have?\n"))
			print(crit.play(fun))

		# secret backdoor
		elif choice == '14':
			print(crit)

		# some unknown choice
		else:
			print(f"Sorry, but {choice} isn't a valid choice.")
if __name__ == '__main__':
	main()