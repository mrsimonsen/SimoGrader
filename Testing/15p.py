from subprocess import run
from os import getcwd
import sys

import pig_latin

#15p
file = "pig_latin.py"
passed = 0
total = 0
failed = []

def main():
	global score, total
	simple()
	try:
		verbose = sys.argv[1]!='simple'
	except:
		verbose = True
	if verbose:
		print(f"Passed {passed} out of {total} tests.")
		if len(failed) > 0:
			print("Failed:")
			for i in failed:
				print(f"\t* {i}")

def simple():
	global score, total
	test1()
	test2()
	test3()
	test4()
	test5()
	test6()
	test7()
	test8()
	test9()
	test10()
	test11()
	hidden1()
	print(f"{passed}/{total}")

def test1():
	global total, passed
	total += 1
	correct = "aeiou"
	try:
		result = pig_latin.VOWELS
	except:
		result = ''
	if result == correct:
		passed += 1
	else:
		failed.append('test1')

def test2():
	global total, passed
	total += 1
	correct = 'appleway'
	try:
		result = pig_latin.way_end('apple')
	except:
		result = ''
	if result == correct:
		passed += 1
	else:
		failed.append('test2')

def test3():
	global total, passed
	total += 1
	correct = 'appyhay'
	try:
		result = pig_latin.ay_end('happy', 1)
	except:
		result = ''
	if result == correct:
		passed += 1
	else:
		failed.append('test3')

def test4():
	global total, passed
	total += 1
	correct = ["appyhay 5 applesway\n"]
	try:
		result = pig_latin.translate(["Happy 5 appLes"])
	except:
		result = ''
	if result == correct:
		passed += 1
	else:
		failed.append('test4')

def test5():
	global total, passed
	total += 1
	inputs = "nothing.txt"
	out = "Welcome to the Pig Latin Translator!\n"
	out += "What is the name of the file:\n"
	out += "Message stored in 'pig.txt'\n"
	correct = [out, ['1error']]
	try:
		result = [catchOutput(inputs)]
	except:
		result = ['no output']
	try:
		result.append(pig_latin.read('nothing.txt'))
	except IOError:
		result.append("IOError not caught")
	if result == correct:
		passed += 1
	else:
		failed.append('test5')

def test6():
	global total, passed
	total += 1
	try:
		pig_latin.write(["Some message!\nwith 2 lines!\n"])
		result = pig_latin.read('pig.txt')
	except:
		result = "Read/Write don't work"
	correct = ["Some message!\n", "with 2 lines!\n"]
	if result == correct:
		passed += 1
	else:
		failed.append('test6')

def test7():
	global total, passed
	total += 1
	correct = "appyhay!"
	try:
		result = pig_latin.ay_end("happy!", 1)
	except:
		result = ''
	if result == correct:
		passed += 1
	else:
		failed.append('test7')

def test8():
	global total, passed
	total += 1
	correct = "eggway,"
	try:
		result = pig_latin.way_end("egg,")
	except:
		result = ''
	if result == correct:
		passed += 1
	else:
		failed.append('test8')
def test9():
	global total, passed

	total += 1
	correct = '.,!?'
	try:
		result = pig_latin.END
		if result == correct:
			passed += 1
		else:
			failed.append('test9')
	except:
		failed.append('test9')

def test10():
	global total, passed
	total += 1
	correct = ["oolschay?\n","oolcay\n"]
	try:
		result = pig_latin.translate(["school?","cool"])
	except:
		result = []
	if result == correct:
		passed += 1
	else:
		failed.append('test10')

def test11():
	global total, passed
	total += 1
	correct = ["enigmaway.\n"]
	try:
		result = pig_latin.translate(["enigma."])
	except:
		result = []
	if result == correct:
		passed += 1
	else:
		failed.append('test11')

def hidden1():
	global total, passed
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
	try:
		pig_latin.write(pig_latin.translate(pig_latin.read('test.txt')))
		with open('pig.txt','r') as f:
			result = f.read()
	except:
		result = ''
	if result == correct:
		passed += 3
	else:
		failed.append('hidden1')

# setup methods
def catchOutput(inputs=None, seed=''):
	p = run(f"python3 {file} {seed}", capture_output=True, text=True, shell=True, input=inputs)
	return p.stdout

if __name__ == "__main__":
	main()
