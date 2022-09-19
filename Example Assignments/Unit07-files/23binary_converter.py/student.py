def write(binary):
	pass

def convert(num):
	binary = f"{num:b}"
	return binary

#Do not edit the code below this line
#################################################
def main():
	valid = False
	while not valid:
		try:
			num = int(input("Enter a number:\n"))
			valid = True
		except ValueError:
			print("That wasn't an integer, try again.")
	binary = convert(num)
	print(binary)
	write(binary)