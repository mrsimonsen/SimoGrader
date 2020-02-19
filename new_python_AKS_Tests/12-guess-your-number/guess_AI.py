#Mr. Simonsen
#14

import random

def end(tries, user):
    if tries <= 6 and user == 'correct':
        return f"I knew I could beat you, and in {tries} tries too!"
    else:
        return "I ran out of tries! You bested me!"

def high_low(low, high, guess, user, tries, play):
    if tries < 6:
        if user.lower() == 'high':
            high = guess -1
            tries += 1
            return low, high, tries, play
        elif user.lower() == 'low':
            low = guess +1
            tries += 1
            return low, high, tries, play
        elif user.lower() == 'correct':
            return low, high, tries, False
    else:
        return low, high, tries, False


def main():
    print("I am a special mind-reading machine and will guess the number you're thinking of between 1 and 100 in 6 tries or less.")
    print("After each guess, tell me if I'm 'high', 'low', or 'correct'.")

    high = 100
    low = 1
    play = True
    guess = random.randint(low,high)
    tries = 1
    user = ''
    while play:
        print(f"For try {tries} I guess {guess}")
        user = ''
        while user not in ('high','low','correct'):
            user = input("Am I 'high', 'low', or 'correct'? ")
        low, high, tries, play = high_low(low, high, guess, user, tries, play)
        guess = random.randint(low, high)
    print(end(tries, user))
