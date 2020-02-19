#Mr. Simonsen
#14
import random

def coin(flips):
    count = 0
    heads = 0
    tails = 0
    while count < flips:
        if random.randrange(2):
            heads += 1
        else:
            tails += 1
        count += 1
    return count, heads, tails

def main():
    flips = int(input("How many coin flips do you want?"))
    c,h,t = coin(flips)
    print("The coin has been flipped {} times.\nHeads: {}\t Tails: {}".format(c,h,t))
