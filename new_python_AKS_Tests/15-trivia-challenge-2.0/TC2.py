#Mr. Simonsen
#14

import sys, pickle

def hs_table(hs):
    rep =''
    for i in hs:
        rep += f"Name: {i[1]}\tScore: {i[0]}\n"
        return rep
        
def sortNsave(score, name, hs):
    hs.append((score,name))
    hs.sort(reverse=True)
    hs = hs[:3]
    f = open_file('highscores.dat', 'wb')
    pickle.dump(hs, f)
    f.close()
    return hs

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print(f"Unable to open the file {file_name} Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)

    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    points = next_line(the_file)
    if points:
        points = int(points)

    return category, question, answers, correct, explanation, points

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print(f"\t\t{title}\n")


def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get first block
    category, question, answers, correct, explanation, points = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print(f"\t{i + 1} - {answers[i]}")

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += points
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print(f"Score: {score}\n\n")

        # get next block
        category, question, answers, correct, explanation, points = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print(f"You're final score is {score})
    f = open_file('highscores.dat', 'rb')
    hs = pickle.load(f)
    f.close()
    if score >= hs[2][0]:
        name = input("You made the highscore list, give me 3 initials: ")[:3].upper()
        hs = sortNsave(score, name, hs)
    print(hs_table(hs))
