#Mr. Simonsen
#14

start = int(input("What is the starting number?\n"))
end = int(input("What is the ending number?\n"))
step = int(input("How much should I count by?\n"))
print(f"Counting from {start} to {end} by {step}:")

if step > 0:
	end += 1
else:
	end -= 1

rep = ''
for i in range(start, end, step):
	rep += f"{i} "
print(rep)