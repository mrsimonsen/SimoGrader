#Name
#Period

#leave this code or testing won't work
import random, sys
if len(sys.argv)-1:
	random.seed(int(sys.argv[1]))
#########################################################

seed = input("Press enter to see the results.\n")
if seed:
	random.seed(int(seed))

print("The coin was flipped 5 times.")
