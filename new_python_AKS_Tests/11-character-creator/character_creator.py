#Mr. Simonsen
#14

MENU = '''
\t\t\t ____
\t\t\t|Menu|
\t\t0 - Quit
\t\t1 - View Attributes and Pool
\t\t2 - Add to Attribute
\t\t3 - Remove from Attribute'''

def add(attr, amt, atts):
	if attr in atts:
		if amt <= atts["Pool"]:
			atts["Pool"] -= amt
			atts[attr] += amt
			return f"{amt} added to {attr}"
		else:
			return f"{amt} is more points than you have left in your pool"
	else:
		return f"'{attr}' is not a valid attribute"

def remove(attr, amt, atts):
	if attr in atts:
		if amt <= atts[attr]:
			atts["Pool"] += amt
			atts[attr] -= amt
			return f"{amt} removed from {attr}"
		else:
			return f"{amt} is more points than you have left in {attr}"
	else:
		return f"'{attr}' is not a valid attribute"

def table(atts):
	rep = f'''
______________________________
Strength\t|\t{atts['Strength']}
Dexterity\t|\t{atts['Dexterity']}
Constitution\t|\t{atts['Constitution']}
Wisdom\t\t|\t{atts['Wisdom']}
Intelligence\t|\t{atts['Intelligence']}
Charisma\t|\t{atts['Constitution']}
Pool\t\t|\t{atts['Pool']}
______________________________'''
	return rep

def main():
	atts = {'Strength':0, 'Dexterity':0, 'Constitution':0, 'Wisdom':0, 'Intelligence':0, 'Charisma':0, 'Pool':72}
	play = True
	while play:
		print(MENU)
		choice = input("What's your choice?\n")
		if choice == '1':
			print(table(atts))
		elif choice == '2':
			attr = input("What attribute would like to add points to?\n").title()
			amt = int(input("How many points would you like to add?\n"))
			print(add(attr, amt, atts))
		elif choice == '3':
			attr = input("What attribute would like to remove points from?\n").title()
			amt = int(input("How many points would you like to remove?\n"))
			print(remove(attr, amt, atts))
		elif choice == '0':
			print("Goodbye.")
			play = False
		else:
			print(f"{choice} is not a valad menu option.")

if __name__=="__main__":
	main()