import random

def main():
    total = 0
    score = 0

#def test1():
    total+=1
    random.seed(0)
    if student.coin(100) == (100,50,50):
        score += 1
#def test2():
    total+=1
    random.seed(14)
    if student.coin(100) == (100,58,42) or student.coin(100) == (100,42,58):
        score += 1
#def test3():
    total+=1
    random.seed(14)
    if student.coin(-100) == (0,0,0):
        score += 1

    #hidden test
    total+=1
    random.seed(0)
    if student.coin(25) == (25,16,9) or student.coin(100) == (25,9,19):
        score += 1


        print(f"{score}/{total}")

if __name__ == '__main__':
    main()
