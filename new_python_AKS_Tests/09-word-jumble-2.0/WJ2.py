#Mr. Simonsen
#14

import random
WORDS = ("python",
        "jumble",
        "easy",
        "difficult",
        "answer")
HINTS = ('coding language',
        'name of the game',
        'not hard',
        'not easy',
        "what you're looking for")

def setup(WORDS, HINTS):
    # pick one word randomly from the sequence
    i = random.randrange(len(WORDS))
    # create a variable to use later to see if the guess is correct
    correct = WORDS[i]
    word = correct
    hint = HINTS[i]
    # create a jumbled version of the word
    jumble =""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    return correct, jumble, hint

def guessing(correct, guess, hint, hint_used):
    if guess == correct:
        rep = "That's it!  You guessed it!\n"
        playing = False
    elif guess == '?':
        rep = hint
        playing = True
        hint_used = True
    else:
        rep = "That's not it. Try again.\nType '?' if you want a hint."
        playing = True
    return playing, rep, hint_used

def end(hint_used):
    if hint_used:
        rep = "Try to not use a hint next time.\nThanks for playing."
    else:
        rep = "Good job not using a hint!\nThanks for playing."
    return rep

def main():
    correct, jumble, hint = setup(WORDS, HINTS)
    playing = True
    hint_used = False
    # start the game
    print(
    """
           Welcome to Word Jumble!

   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)""")
    print("The jumble is:", jumble)
    while playing:
        guess = input("Your guess: ")
        playing, text, hint_used = guessing(correct, guess, hint, hint_used)
        print(text)
    print(end(hint_used))
