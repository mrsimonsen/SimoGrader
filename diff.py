def main():
#	with open('correct.txt','r') as f:
#		correct = f.read();
#	with open('result.txt','r') as f:
#		result = f.read();
	with open('1.txt','r') as f:
		correct = f.read()
	with open('2.txt','r') as f:
		result = f.read()
	print(diff(result, correct))

def splitter(thing):
	lines = []
	temp = ''
	for i in thing:
		temp += i
		if i == '\n':
			lines.append(temp)
			temp = ''
	if len(lines)<1:
		lines.append(temp)
	return lines

def locate(rList, cList):
	rs = len(rList)
	cs = len(cList)
	if rs > cs:
		#last line of cList is the difference
		return cs-1,0
	elif cs > rs:
		#last line of rList is the difference
		return rs-1,0
	else:#lists are the same length
		for line in range(cs):
			rline = rList[line]
			cline = cList[line]
			if len(rline) != len(cline):
				#check the last character
				if rline[-1] != cline[-1]:
					return line, -1
			if len(rline) > len(cline):
				length = len(cline)
			else:
				length = len(rline)
			for char in range(length):
				if rline[char]!= cline[char]:
					return line,char
	return 404,404


def diff(result, correct):
	rList = splitter(result)
	cList = splitter(correct)
	line, index = locate(rList,cList)
	try:	
		rchar = rList[line][index]
	except IndexError as e:
		print(f"result char error: {e}")
		rchar = "<nothing>"
	try:
		cchar = cList[line][index]
	except IndexError as e:
		print(f"correct char error: {e}")
		cchar = "<nothing>"
	print(len(cList),len(rList))
	return line,index,rchar,cchar


if __name__ == "__main__":
	main()
