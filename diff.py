def main():
	with open('correct.txt','r') as f:
		correct = f.read();
	with open('result.txt','r') as f:
		result = f.read();
#	with open('1.txt','r') as f:
#		correct = f.read()
#	with open('2.txt','r') as f:
#		result = f.read()
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
	index = 404
	rl = len(rList)
	cl = len(cList)
	small = 0
	if rl<cl:
		small = rl
	else:
		small = cl
	listLength = range(small)
	for line in listLength:
		if rList[line] == cList[line]:
			#don't need to run if the current lines are the same
			continue
		else:
			rl = len(rList[line])
			cl = len(cList[line])
			if rl < cl:
				small = rl
			else:
				small = cl
			for index in range(small):#seach the parts for a difference
				if rList[line][index] != cList[line][index]:
					return line, index
			#runs if the difference is after the end of the short line
			if rl != cl:
				if rl < cl:
					return line, rl
				else:
					return line, cl
	return line, index


def diff(result, correct):
	rList = splitter(result)
	cList = splitter(correct)
	line, index = locate(rList,cList)
	if index == 404:
		if len(rList[line])<len(cList[line]):
			rdiff = rList[line][-1]
			try:
				cdiff = cList[line][len(rList[line])]
			except IndexError:
				cdiff = "<nothing>"
		else:
			cdiff = cList[line][-1]
			try:
				rdiff = rList[line][len(cList[line])]
			except IndexError:
				rdiff = "<nothing>"
	#FIXME
	return line, index, rdiff, cdiff


if __name__ == "__main__":
	main()
