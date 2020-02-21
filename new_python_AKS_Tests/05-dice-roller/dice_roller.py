import random

num = int(input("How many dice would you like to roll?\n"))
d = int(input ("How many sides do the dice have?\n"))
seed = input(f"Press enter to roll {num}x d{d}.\n")
if seed:
	random.seed(seed)

sum = 0
for i in range(num):
	value = random.randrange(1,d)
	sum += value
	print(f"Roll {i+1}: {value}")

print(f"Total: {sum}")