from subprocess import run
from os import getcwd
import sys

#09p
file = "WJ2.py"
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
	hidden1()
	print(f"{passed}/{total}")

def test1():
	global total, passed
	total += 1
	inputs = "\n"
	correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n(Press the enter key at the prompt to quit.)\n\n"
	correct += "The jumble is: asey\n\nYour guess:\n"
	correct += "Goodbye.\n"
	result = catchOutput(inputs, '7')
	if result == correct:
		passed += 1
	else:
		failed.append("test1")

def test2():
	global total, passed
	total += 1
	inputs = "blah\n\n"
	correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n(Press the enter key at the prompt to quit.)\n\n"
	correct += "The jumble is: swaenr\n\nYour guess:\n"
	correct += "Sorry, that's not it.\nType '?' if you want a hint.\n"
	correct += "Your guess:\nGoodbye.\n"
	result = catchOutput(inputs, '5')
	if result == correct:
		passed += 1
	else:
		failed.append('test2')

def test3():
	global total, passed
	total += 1
	inputs = "?\n\n"
	correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n(Press the enter key at the prompt to quit.)\n\n"
	correct += "The jumble is: ljbuem\n\nYour guess:\n"
	correct += "the name of the game\n"
	correct += "Your guess:\nGoodbye.\n"
	result = catchOutput(inputs, '1')
	if result == correct:
		passed += 1
	else:
		failed.append('test3')

def test4():
	global total, passed
	total += 1
	inputs="python\n"
	correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n(Press the enter key at the prompt to quit.)\n\n"
	correct += "The jumble is: pyotnh\n\nYour guess:\n"
	correct += "That's it! You guessed it!\n"
	correct += "Good job not using a hint!\n"
	correct += "Thanks for playing.\n"
	result = catchOutput(inputs, '2')
	if result == correct:
		passed += 1
	else:
		failed.append('test4')

def test5():
	global total, passed
	total += 1
	inputs="?\ndifficult\n"
	correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n(Press the enter key at the prompt to quit.)\n\n"
	correct += "The jumble is: udflctfii\n\nYour guess:\n"
	correct += "not easy\n"
	correct += "Your guess:\n"
	correct += "That's it! You guessed it!\n"
	correct += "Try to not use a hint next time.\n"
	correct += "Thanks for playing.\n"
	result = catchOutput(inputs, '0')
	if result == correct:
		passed += 1
	else:
		failed.append('test5')

def hidden1():
	global total, passed
	total += 2
	inputs = "guess\n?\n?\npython\n"
	correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n(Press the enter key at the prompt to quit.)\n\n"
	correct += "The jumble is: pyotnh\n\nYour guess:\n"
	correct += "Sorry, that's not it.\nType '?' if you want a hint.\n"
	correct += "Your guess:\na slithery coding language\n"
	correct += "Your guess:\na slithery coding language\n"
	correct += "Your guess:\nThat's it! You guessed it!\n"
	correct += "Try to not use a hint next time.\n"
	correct += "Thanks for playing.\n"
	result = catchOutput(inputs, '2')
	if result == correct:
		passed += 2
	else:
		failed.append('hidden1')

# setup methods
def catchOutput(inputs=None, seed=''):
	p = run(f"python3 {file} {seed}", capture_output=True, text=True, shell=True, input=inputs)
	return p.stdout

if __name__ == "__main__":
	main()
