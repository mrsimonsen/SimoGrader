import Tools

def main():
	print("\tWelcome to the Caesar Cipher!\nThis utility will let you encrypt and decrypt a message from a file you provide.")

	choice = -1
	while choice != 0:
		print('''
		MENU
	Option 1: Encrypt Message
	Option 2: Decrypt Message
	Option 3: Letter Distribution Analysis
	Option 0: Exit Program
''')
		message = None
		choice = None
		while choice not in range(4):
			try:
				choice = int(input("Choose an option:\n"))
			except ValueError:
				print("That wasn't a number.")

		if choice and Tools.ask_yn("Is the message in a file?\n"):
			message = Tools.open_file(input("What is the name of the file?\n"))
		if choice == 1:
			key = Tools.get_cipher()
			if message:
				Tools.write(Tools.encrypt(message, key))
			else:
				Tools.write(Tools.encrypt(input("What is the message?\n"), key))

		elif choice == 2:
			key = Tools.get_cipher()
			if message:
				Tools.write(Tools.decrypt(message, key))
			else:
				Tools.write(Tools.decrypt(input("What is the message?\n"), key))

		elif choice == 3:
			if message:
				Tools.analysis(message)
			else:
				print("Letter Distribution Analysis requires the message to be in a text file.")