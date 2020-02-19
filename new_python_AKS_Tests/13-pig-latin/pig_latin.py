#Mr. Simonsen
#14

END = ".,!?"
VOWELS = "aeiouy"

def way_end(word):
    new = ""
    if word[-1] in END:
        new = word[:-1] + "way" + word[-1]
    else:
        new = word + "way"
    return new

def ay_end(word, i):
    new = ""
    if word[-1] in END:
        new = word[i:-1] + word[:i] + "ay" + word[-1]
    else:
        new = word[i:] + word[:i] + "ay"
    return new

def translator(message):
    words = message.split(" ")
    pig = ''
    #determine if the the word begins with a vowel
    for word in words:
        if word[0].lower() in VOWELS:
            pig += way_end(word)
        else:#it starts with a consonant
            #need to find out how many letters to take from the front
            for letter in word:
                if letter.lower() in VOWELS:
                    index = word.index(letter)
                    break #only interested in the first vowel
            pig += ay_end(word, index)
    return pig.capitalize()

def main():
  print("Welcome to the Pig Latin Translator!")
  message = input("Please enter a word to translate:\n")
  pig = translator(message)
  print(f"The translation is:\n\n{pig}")
  print("\nGoodbye!")

if __name__ == '__main__':
    main()
