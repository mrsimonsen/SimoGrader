def ask_yn(question):
	response = 'a'
	while response not in ('y','yes','no','n'):
		response = input(question).lower()
	if 'y' in response:
		return True
	else:
		return False

def get_cipher():
	key = 0
	while key not in range(1,26):
		try:
			key = int(input("What is the cipher key?\n"))
		except ValueError:
			print("That wasn't a number.")
		else:
			if key in range(1,26):
				return key
			else:
				print("Cipher key must be between 1 and 25 inclusive.")

def open_file(name):
	message = None
	try:
		file = open(name,'r')
		message = file.read()
		file.close()
	except IOError:
		print(f"Couldn't find \"{name}\".")
	return message

def write(message):
	name = input("What do you want to call the output file?\n")
	if len(name) < 4 or name[-4:] != ".txt":
		name += ".txt"
	file = open(name,'w')
	file.write(message)
	file.close()

def decrypt(message, key):
	return encrypt(message, -key)

def encrypt(message, key):
	new = ""
	if key < 0:
		key += 26

	for char in message:
		num = ord(char)
		if 65 <= num <= 90:
			num += key
			if num > 90:
				num -= 26
		elif 97 <= num <= 122:
			num += key
			if num > 122:
				num -= 26
		new += chr(num)
	return new

def analysis(message):
	dist = [0]*26
	for char in message.lower():
		i = ord(char)
		if 97 <= i <= 122:
			dist[i-97] += 1

	for i in range(26):
		print(f"{chr(i+97)}: {dist[i]:02} {'*'*dist[i]}")
