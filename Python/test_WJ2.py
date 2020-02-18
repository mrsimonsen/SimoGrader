import random

def main():
    total = 0
    score = 0

#def test_setup1():
    total+=1
    random.seed(0)
    W = ('one','two','three','four')
    H = ('1','2','3','4')
    if student.setup(W, H) == ('four', 'rfuo', '4'):
        score += 1

#def test_setup2():
    total+=1
    random.seed(14)
    W = ('one','two','three','four')
    H = ('1','2','3','4')
    if student.setup(W, H) == ('one', 'eon', '1'):
        score += 1

#def test_guessing1():
    total+=1
    if student.guessing('bob', 'bob', 'name', False) == (False,"That's it!  You guessed it!\n",False):
        score += 1

#def test_guessing2():
    total+=1
    if student.guessing('bob', '?', 'name', False) == (True,"name",True):
        score += 1

#def test_guessing3():
    total+=1
    if student.guessing('bob', 'sue', 'name', True) == (True,"That's not it. Try again.\nType '?' if you want a hint.",True):
        score += 1

#def test_end1():
    total+=1
    if student.end(0) == "Good job not using a hint!\nThanks for playing.":
        score += 1

#def test_end2():
    total+=1
    if student.end(True) == "Try to not use a hint next time.\nThanks for playing.":
        score += 1

#hidden tests
    total+=1
    if student.guessing('word','?','thing',False) = (True,'thing',True):
        score += 1

    total += 1
    random.seed(2)
    W = ('this','word','or','that')
    H = (1,2,3,4)
    if student.setup(W,H) == ('this', 'thsi', 1):
        score+=1

    print(f"{score}/{total}")

if __name__ == '__main__':
    main()
