#Mr. Simonsen
#14

tri_char = input("Enter a character:\n")
tri_height = int(input("Enter a triangle height:\n"))

tri = ''
for i in range(tri_height+1):
	print(f"{tri_char} " * i)

