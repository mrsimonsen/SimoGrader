#Mr. Simonsen
#14

#leave this code or testing won't work
import random, sys
if len(sys.argv)-1:
	random.seed(int(sys.argv[1]))
#########################################################

print("You crack open your cookie and your fortune falls out:")
fortune = random.randrange(5)
if fortune == 0:
	print("Help! I’m being held prisoner in a fortune cookie bakery!")
elif fortune == 1:
	print("Cookie said: \"You really crack me up.\"")
elif fortune == 2:
	print("You are not illiterate.")
elif fortune == 3:
	print("You will read this and say \"Geez! I could come wp with better fortunes than that!\"")
elif fortune == 4:
	print("This cookie is never gonna give you up, never gonna let your down.")