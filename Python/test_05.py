def main():
    total = 0
    score = 0

#def test1():
    total+=1
    random.seed(0)
    if student.roll(2,6) == 8:
        score += 1

#def test2():
    total+=1
    random.seed(14)
    if student.roll(5,10) == 30:
        score += 1

#def test3():
    total+=1
    random.seed(10)
    if student.roll(10,6) == 33:
        score += 1

#hidden test
    total+=1
    random.seed(5)
    if student.roll(2, 14) == 15:
        score += 1

    print(f"{score}/{total}")

if __name__ == '__main__':
    main()
