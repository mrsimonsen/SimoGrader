#Mr. Simonsen
#14

def reverse(message):
    rep = ''
    for letter in message:
        rep = letter + rep
    return rep

def easy_reverse(message):
    return message[::-1]

def main():
    message = input("What is your message?\n")
    print(reverse(message))
    print(easy_reverse(message))
