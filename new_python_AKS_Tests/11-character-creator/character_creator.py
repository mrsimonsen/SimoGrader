#Mr. Simonsen
#14

def add(attr, amt, character):
    if attr in character:
        if amt <= character["Pool"]:
            character["Pool"] -= amt
            character[attr] += amt
            message = f"{amt} added to {attr}"
        else:
            message = f"{amt} is more points than you have left in your pool"
    else:
        message = f"{attr} is not a valid attribute"
    return message

def remove(attr, amt, character):
    if attr in character:
        if amt <= character[attr]:
            character["Pool"] += amt
            character[attr] -= amt
            message = f"{amt} removed from {attr}"
        else:
            message = f"{amt} is more points than you have left in {attr}"
    else:
        message = f"{attr} is not a valid attribute"
    return message

def main():
    character = {'Strength':0,
                'Dexterity':0,
                'Consitiution':0,
                'Wisdom':0,
                'Intellgence':0,
                'Charisma':0,
                'Pool':65}
    menu = '''\t\t\t ____
\t\t\t|Menu|
\t\t0 - Quit
\t\t1 - View Attributes and Pool
\t\t2 - Add to Attrubute
\t\t3 - Remove from Attribute'''
    play = True
    while play:
        print(menu)
        choice = input("What's your choice? ")
        if choice == '1':
            print(character)
        elif choice == '2':
            attr = input("What attribute would like to add points to?\n").title()
            amt = int(input("How many points would you like to add? "))
            message = add(attr, amt, character)
            print(message)
        elif choice == '3':
            attr = input("What attribute would like to remove points from?\n")
            amt = int(input("How many points would you like to remove? "))
            message = remove(attr, amt, character)
            print(message)
        elif choice == '0':
            print("Exiting...")
            play = False
        else:
            print(f"{choice} is not a valad menu option.")
