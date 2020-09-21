from subprocess import run
from os import chdir, system
p = ('00p','01p','02p','03p','04p','05p','06p','07p','08p','09p','10p','11p','12p','13p','14p','15p')
j = ('00j','01j','02j','03j','04j','05j','06j','07j','08j','09j','10j','11j','12j','13j','14j','15j','16j','17j','18j','19j','20j','21j')
assignments = []
notFinished = True

while notFinished:
	notValid = True
	while notValid:
		pre = input("Enter repository prefix (assignment code)(type 'done' when finished): ")
		if (pre in p or pre in j) or pre == 'done':
			notValid = False
		else:
			print(f"\"{pre}\" is not valid, try again.")
	if pre != 'done':
		assignments.append(pre)
	else: 
		notFinished = False
	print(assignments)
for i in assignments:
	f = open('assignment.txt','w')
	f.write(i)
	f.close()
	system('./all.sh')
print('Operation Complete',assignments)
