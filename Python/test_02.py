import random

def main():
    total = 0
    score = 0

#def test1():
    total+=1
    random.seed(2)
    if student.cookie() == "Help! I’m being held prisoner in a fortune cookie bakery!":
        score += 1

#def test2():
    total+=1
    random.seed(1)
    if student.cookie() == "Cookie said: \"You really crack me up.\"":
        score += 1

#def test3():
    total+=1
    random.seed(7)
    if student.cookie() == "You are not illiterate.":
        score += 1

#def test4():
    total+=1
    random.seed(0)
    if student.cookie() == "You will read this and say \"Geez! I could come wp with better fortunes than that!\"":
        score += 1

#def test5():
    total+=1
    random.seed(5)
    if student.cookie() == "This cookie is never gonna give you up, never gonna let your down.":
        score += 1

#no hidden tests for this assignment
    print(f"{score}/{total}")

if __name__ == '__main__':
    main()
