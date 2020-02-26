#Mr. Simonsen
#14

#leave this code or testing won't work
import random, sys
if len(sys.argv)-1:
	random.seed(int(sys.argv[1]))
#########################################################

message = input("What is the message to scramble?\n")
words = message.split(" ")
print(f"There are {len(words)} words in the message.")
print("Here's the shuffeled message:")
random.shuffle(words)
print(" ".join(words))