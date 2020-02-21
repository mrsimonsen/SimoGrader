#Mr. Simonsen
#14
import random

coins = int(input("How many times do you want to flip the coin?\n"))
seed = input("Press enter to see the results.\n")
if seed:
	random.seed(int(seed))
count = 0
heads = 0
while count < coins:
	if random.randrange(2):
		heads += 1
	count += 1
print(f"The coin was flipped {coins} times.\nHeads: {heads}\tTails: {coins-heads}")