from subprocess import run
from os import getcwd
file = "WJ2.py"

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
	inputs = "\n"
	correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n(Press the enter key at the prompt to quit.)\n\n"
	correct += "The jumble is: asey\n\nYour guess:\n"
	correct += "Goodbye.\n"
	result = catchOutput(inputs, '7')
	if result == correct:
		score += 1
		
	total += 1 
	#def test_2(self):
	inputs = "blah\n\n"
	correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n(Press the enter key at the prompt to quit.)\n\n"
	correct += "The jumble is: swaenr\n\nYour guess:\n"
	correct += "Sorry, that's not it.\nType '?' if you want a hint.\n"
	correct += "Your guess:\nGoodbye.\n"
	result = catchOutput(inputs, '5')
	if result == correct:
		score += 1
		
	total += 1
	#def test_3(self):
	inputs = "?\n\n"
	correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n(Press the enter key at the prompt to quit.)\n\n"
	correct += "The jumble is: ljbuem\n\nYour guess:\n"
	correct += "the name of the game\n"
	correct += "Your guess:\nGoodbye.\n"
	result = catchOutput(inputs, '1')
	if result == correct:
		score += 1
		
	total += 1
	#def test_4(self):
	inputs="python\n"
	correct = "\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n(Press the enter key at the prompt to quit.)\n\n"
	correct += "The jumble is: pyotnh\n\nYour guess:\n"
	correct += "That's it! You guessed it!\n"
	correct += "Good job not using a hint!\n"
	correct += "Thanks for playing.\n"
	result = catchOutput(inputs, '2')
	if result == correct:
		score += 1
	
	total += 1
	#def test_5(self):
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
		score += 1
		
	#hidden tests
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
		score += 2
		
	return f"{score}/{total}"

if __name__ == "__main__":
	print(main())
