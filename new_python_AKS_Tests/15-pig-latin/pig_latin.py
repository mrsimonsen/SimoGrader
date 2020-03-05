#Mr. Simonsen
#14

END = '.,!?'
VOWELS = 'aeiou'

def way_end(word):
	new = ''
	end = False
	if '\n' == word[-1]:
		end = True
		word = word[:-1]
	if word[-1] in END:
		new = word[:-1] + 'way' + word[-1]
	else:
		new = word + 'way'
	if end:
		new += '\n'
	return new

def ay_end(word, i):
	new = ''
	end = False
	if '\n' == word[-1]:
		end = True
		word = word[:-1]
	if word[-1] in END:
		new = word[i:-1] + word[:i] + 'ay' + word[-1]
	else:
		new = word[i:] + word[:i] + 'ay'
	if end:
		new += '\n'
	return new

def translate(message):
	words = message.split(' ')
	pig = []
	for w in words:
		if w[0].lower() in VOWELS:
			pig.append(way_end(w))
		elif w[0].isalpha():
			for letter in w:
				if letter.lower() in VOWELS:
					index = w.index(letter)
					break
			pig.append(ay_end(w, index))
		else:
			pig.append(w)
	new = ' '.join(pig)
	return new.lower()

def read(file):
	try:
		f = open(file, 'r')
		message = f.read()
		f.close()
		return message
	except:
		return '1error'

def write(message):
	f = open('pig.txt', 'w')
	f.write(message)
	f.close()
	
def main():
	print("Welcome to the Pig Latin Translator!")
	file = input("What is the name of the file:\n")
	message = read(file)
	new = translate(message)
	write(new)
	print("Message stored in 'pig.txt'")
	
if __name__ == "__main__":
	main()
