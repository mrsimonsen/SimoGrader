#Name
#Period

import random

seed = input("Press enter to crack open your cookie and read your fortune.\n")
if seed:
	random.seed(int(seed))
print("Help! I’m being held prisoner in a fortune cookie bakery!")
