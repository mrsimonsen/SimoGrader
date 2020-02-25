#Mr. Simonsen
#14
import random, sys

if len(sys.argv)-1:
	random.seed(sys.argv[1])

coins = int(input("How many times do you want to flip the coin?\n"))
count = 0
heads = 0
while count < coins:
	if random.randrange(2):
		heads += 1
	count += 1
print(f"The coin was flipped {coins} times.\nHeads: {heads}\tTails: {coins-heads}")