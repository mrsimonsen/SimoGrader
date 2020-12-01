from subprocess import run
from os import getcwd
file = "pig_latin.py"
import pig_latin

# setup methods
def catchOutput(inputs=None, seed=''):
	cwd = getcwd()
	p = run(f"python3 {file} {seed}", capture_output=True, text=True, cwd=cwd, shell=True, input=inputs)
	return p.stdout

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
	correct = ["appyhay 5 applesway\n"]
	correct2 = ["appyhay 5 applesway"]
	result = pig_latin.translate(["Happy 5 appLes"])
	if result == correct or result == correct2:
		score += 1

	total += 1
	#def test_5_6(self):
	#A
	inputs = "nothing.txt"
	out = "Welcome to the Pig Latin Translator!\n"
	out += "What is the name of the file:\n"
	out += "--Could not open file!--\n"
	correct = (out, '1error')
	result = (catchOutput(inputs), pig_latin.read('nothing.txt'))
	if result == correct:
		score += 1

	total += 1
	#B
	pig_latin.write("Some message!\nwith 2 lines!\n")
	result = pig_latin.read('pig.txt')
	correct = ["Some message!", "with 2 lines!"]
	if result == correct:
		score += 1

	total += 1
	#def test_7(self):
	#A7
	correct = "appyhay!"
	result = pig_latin.ay_end("happy!", 1)
	if result == correct:
		score += 1
	
	#B8
	total += 1
	correct = "eggway,"
	result = pig_latin.way_end("egg,")
	if result == correct:
		score += 1
	
	#C9
	total += 1
	correct = '.,!?'
	result = pig_latin.END
	if result == correct:
		score += 1
	
	total += 1
	#def test_8(self):
	#A10
	correct = ["oolschay?\n","oolcay\n"]
	result = pig_latin.translate(["school?","cool"])
	if result == correct:
		score += 1

	#B11
	total += 1
	correct = ["enigmaway.\n"]
	result = pig_latin.translate(["enigma."])
	if result == correct:
		score += 1
		
	#hidden tests
	total += 3
	with open("test.txt", 'w') as f:
		f.write('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris fringilla felis at magna blandit elementum? Vestibulum eu vehicula mauris.
Aliquam sed dignissim odio. Sed 2commodo in neque ut luctus. Mauris lacinia et nibh at ultrices. Ut euismod purus tellus, at interdum risus aliquet sed. Aliquam non diam 6orci! Aliquam iaculis justo nec ex tincidunt luctus. 4Aliquam nibh justo, tempor eu lacinia a, rhoncus sed est.
Sed eget sapien tortor. Proin eget viverra lorem, sodales elementum neque.
''')
	correct = '''oremlay ipsumway olorday itsay ametway, onsecteturcay adipiscingway elitway. aurismay ingillafray elisfay atway agnamay anditblay elementumway? estibulumvay euway ehiculavay aurismay.
aliquamway edsay ignissimday odioway. edsay 2commodo inway equenay utway uctuslay. aurismay acinialay etway ibhnay atway ultricesway. utway euismodway uruspay ellustay, atway interdumway isusray aliquetway edsay. aliquamway onnay iamday 6orci! aliquamway iaculisway ustojay ecnay exway incidunttay uctuslay. 4aliquam ibhnay ustojay, emportay euway acinialay away, oncusrhay edsay estway.
edsay egetway apiensay ortortay. oinpray egetway iverravay oremlay, odalessay elementumway equenay.
'''
	pig_latin.write(pig_latin.translate(pig_latin.read('test.txt')))
	with open('pig.txt','r') as f:
		result = f.read()
	if result == correct:
		score += 3
	
	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())
