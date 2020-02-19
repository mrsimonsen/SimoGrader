#Mr. Simonsen
#14

import random

def scrambler(words):
    random.shuffle(words)
    rep = " ".join(words)
    return rep

def splitter(message):
    words = message.split(" ")
    return words, len(words)

def main():
    message = input("What is the message to scrable?\n")
    words, num_words = splitter(message)
    print(f"There are {num_words} words in the message")
    print("Here they are shuffled:")
    print(scrambler(words))
