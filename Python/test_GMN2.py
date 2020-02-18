def main():
    total = 0
    score = 0

##def test1():
    total+=1
    if student.hi_low(1, 100, 1) == ("Low", True):
        score += 1

#def test2():
    total+=1
    if student.hi_low(100, 1, 1) == ("High", True):
        score += 1

#def test3():
    total+=1
    if student.hi_low(1, 1, 1) == ("Correct", False):
        score += 1

#def test4():
    total+=1
    if student.hi_low(100, 1, 5) == ("High", False):
        score += 1

#def test5():
    total+=1
    if student.hi_low(1, 100, 5) == ("Low", False):
        score += 1

#def test6():
    total+=1
    if student.end(5, "Correct", 14) == "You guessed it in 5 tries! The number was 14":
        score += 1

#def test7():
    total+=1
    if student.end(6, "Correct", 14) == "You ran out of tries! The number was 14":
        score += 1

#def test8():
    total+=1
    if student.end(1, "Low", 14) == "You ran out of tries! The number was 14":
        score += 1

#def test9():
    total+=1
    if student.end(1, "High", 14) == "You ran out of tries! The number was 14":
        score += 1

#hidden tests
    total+= 1
    if student.end(3,"Low",12) == "You ran out of tries! The number was 12":
        score +=1
    total+=1
    if student.hi_low(20, 50, 5) == ("Low", False):
        score += 1
    total+=1
    if student.hi_low(50, 20, 4) == ("High", True):
        score += 1

    print(f"{score}/{total}")

if __name__ == '__main__':
    main()
