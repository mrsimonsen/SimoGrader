import pickle
python = ('1030','p','python')
java = ('1400','j','java')

def main():
	number = 'a'
	while type(number) != type(0):
		number = input("How many class periods this semester? ")
		try:
			number = int(number)
		except ValueError as e:
			print(f"That wasn't a number\n{e}")
	classes = {}
	for i in range(number):
		is_comp = False
		period = i+1
		r = ask_yn(f"Is period {period} a programming class? ")
		if r:
			if r not in python+java:
				r = ask_prog()
			classes[period] = r
	display(classes)
	if ask_yn("Correct? "):
		export(classes)
	else:
		main()

def export(classes):
	f = open('classes.dat','wb')
	pickle.dump(classes,f)
	f.close()

def display(classes):
	j = []
	p = []
	for i in classes.keys():
		if classes[i] == 'j':
			j.append(i)
		elif classes[i] == 'p':
			p.append(i)
	print(f"{len(p)} python classes, {len(j)} java classes")
	print(f"\tPython: {p}")
	print(f"\tJava: {j}")

def ask_prog():
	r = None
	while r not in (python+java):
		r = input("What programming class is it? ").lower()
	if r in python:
		return 'p'
	elif r in java:
		return 'j'

def ask_yn(question):
	r = None
	yes = ('y','yes')
	no = ('n','no')
	while r not in yes+no+python+java:
		r = input(question).lower()
	if r in no:
		return False
	elif r in java:
		return 'j'
	elif r in python:
		return 'p'
	elif r in yes:
		return True

if __name__ == "__main__":
	main()
