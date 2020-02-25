#Mr. Simonsen
#14

message = input("What is your message?\n")
rev = ''
for letter in message:
	rev = letter + rev
print("\nYour message reversed is:")
print(rev)

#pythonic way
#message[::-1]