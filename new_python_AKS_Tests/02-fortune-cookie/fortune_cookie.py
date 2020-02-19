#Mr. Simonsen
#14
import random

f1 = "Help! I’m being held prisoner in a fortune cookie bakery!"
f2 = "Cookie said: \"You really crack me up.\""
f3 = "You are not illiterate."
f4 = "You will read this and say \"Geez! I could come wp with better fortunes than that!\""
f5 = "This cookie is never gonna give you up, never gonna let your down."

def cookie():
    fortune = random.randrange(5)
    if fortune == 0:
        return f1
    elif fortune == 1:
        return f2
    elif fortune == 2:
        return f3
    elif fortune == 3:
        return f4
    elif fortune == 4:
        return f5
    else:
        return error

def main():
    print("You crack open the cooke and your fortune falls out:")
    print(cookie())
