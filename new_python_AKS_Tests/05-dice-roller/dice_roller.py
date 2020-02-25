#leave this code or testing won't work
import random, sys
if len(sys.argv)-1:
	random.seed(int(sys.argv[1]))
#########################################################

num = int(input("How many dice would you like to roll?\n"))
d = int(input ("How many sides do the dice have?\n"))
print("Rolling {num}x d{d}.")

sum = 0
for i in range(num):
	value = random.randrange(1,d)
	sum += value
	print(f"Roll {i+1}: {value}")

print(f"Total: {sum}")