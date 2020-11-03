from subprocess import run, TimeoutExpired, Popen, PIPE
from os import getcwd
file = "pig_latin.py"
import pig_latin

# setup methods
def catchOutput(inputs=None, seed=''):
	cwd = getcwd()
	result = None
	p = Popen(f"python3 {file} {seed}",stdin=PIPE,stdout=PIPE,shell=True,cwd=cwd, text=True)
	try:
		out = p.communicate(input=inputs, timeout=3)
		result = out[0]
	except TimeoutExpired:
		result = ""
		p.kill()
		run("ps fjx > kill.txt ", shell=True)
		with open('kill.txt','r') as f:
			data = f.readlines()
		k = data[-1].split(" ")
		run(f"kill {k[5]}",shell=True)
	return result
def main():
	total = 0
	score = 0
	
	total += 1
	#def test_1(self):
	correct = "aeiou"
	result = pig_latin.VOWELS
	if result == correct:
		score += 1
	
	total += 1
	#def test_2(self):
	correct = 'appleway'
	result = pig_latin.way_end('apple')
	if result == correct:
		score += 1
	
	total += 1
	#def test_3(self):
	correct = 'appyhay'
	result = pig_latin.ay_end('happy', 1)
	if result == correct:
		score += 1
	
	total += 1
	#def test_4(self):
	correct = "appyhay 5 applesway"
	result = pig_latin.translate("Happy 5 appLes")
	if result == correct:
		score += 1
	
	total += 1
	#def test_5_6(self):
	#A
	inputs = "nothing.txt"
	out = "Welcome to the Pig Latin Translator!\n"
	out += "What is the name of the file:\n"
	out += "Message stored in 'pig.txt'\n"
	correct = (out, '1error')
	result = (catchOutput(inputs), pig_latin.read('nothing.txt'))
	if result == correct:
		score += 1
	total += 1
	#B
	correct = "Some message!\nwith 2 lines!\n"
	pig_latin.write(correct)
	result = pig_latin.read('pig.txt')
	if result == correct:
		score += 1
	
	total += 1
	#def test_7(self):
	#A
	correct = "appyhay!"
	result = pig_latin.ay_end("happy!", 1)
	if result == correct:
		score += 1
	#B
	total += 1
	correct = "eggway,"
	result = pig_latin.way_end("egg,")
	if result == correct:
		score += 1
	#C
	total += 1
	correct = '.,!?'
	result = pig_latin.END
	if result == correct:
		score += 1
	
	total += 1
	#def test_8(self):
	#A
	correct = "oolschay?\n"
	result = pig_latin.ay_end("school?\n", 3)
	if result == correct:
		score += 1
	#B
	total += 1
	correct = "enigmaway.\n"
	result = pig_latin.way_end("enigma.\n")
	if result == correct:
		score += 1
		
	#hidden tests
	total += 3
	f = open("test.txt", 'w')
	f.write('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris fringilla felis at magna blandit elementum? Vestibulum eu vehicula mauris.
Aliquam sed dignissim odio. Sed 2commodo in neque ut luctus. Mauris lacinia et nibh at ultrices. Ut euismod purus tellus, at interdum risus aliquet sed. Aliquam non diam 6orci! Aliquam iaculis justo nec ex tincidunt luctus. 4Aliquam nibh justo, tempor eu lacinia a, rhoncus sed est.
Sed eget sapien tortor. Proin eget viverra lorem, sodales elementum neque.

''')
	f.close()
	correct = '''oremlay ipsumway olorday itsay ametway, onsecteturcay adipiscingway elitway. aurismay ingillafray elisfay atway agnamay anditblay elementumway? estibulumvay euway ehiculavay auris.
aliquammay edsay ignissimday odioway. edsay 2commodo inway equenay utway uctuslay. aurismay acinialay etway ibhnay atway ultricesway. utway euismodway uruspay ellustay, atway interdumway isusray aliquetway edsay. aliquamway onnay iamday 6orci! aliquamway iaculisway ustojay ecnay exway incidunttay uctuslay. 4aliquam ibhnay ustojay, emportay euway acinialay away, oncusrhay edsay est.
sedway egetway apiensay ortortay. oinpray egetway iverravay oremlay, odalessay elementumway eque.
nay
'''
	pig_latin.write(pig_latin.translate(pig_latin.read('test.txt')))
	result = pig_latin.read('pig.txt')
	if result == correct:
		score += 3
	
	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())