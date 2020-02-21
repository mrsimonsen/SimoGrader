#Name
#Period

import random

seed = input("Press enter to see the results.\n")
if seed:
	random.seed(int(seed))

print("The coin was flipped 5 times.")
