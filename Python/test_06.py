def main():
    total = 0
    score = 0

#def test1():
    total+=1
    if student.count(1,10,2) == "1 3 5 7 9 ":
        score += 1

#def test2():
    total+=1
    if student.count(0,10,2) == "0 2 4 6 8 10 ":
        score += 1

#def test3():
    total+=1
    if student.count(0,10,-1) == "":
        score += 1

#def test4():
    total+=1
    if student.count(10,0,-1) == "10 9 8 7 6 5 4 3 2 1 0 ":
        score += 1

#hidden test
    total+=1
    if student.count(0,100,7) == "0 7 14 21 28 35 42 49 56 63 70 77 84 91 98 ":
        score += 1

    print(f"{score}/{total}")

if __name__ == '__main__':
    main()
