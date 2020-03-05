#Name
#Period

def read(file):
	return ''

def write(message):
	pass

def translate(message):
	return message


def main():
	print("Welcome to the Pig Latin Translator!")
	file = input("What is the name of the file:\n")
	message = read(file)
	new = translate(message)
	write(new)
	print("Message stored in 'pig.txt'")
	
if __name__ == "__main__":
	main()