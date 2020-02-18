def main():
    total = 0
    score = 0

#def test1():
    total+=1
    if student.high_low(1,100,50,'correct',1,True) == (1,100,1,False):
        score += 1

#def test2():
    total+=1
    if student.high_low(1,100,20,'low',1,True) == (21,100,2,True):
        score += 1

#def test3():
    total+=1
    if student.high_low(1,100,50,'high',6,True) == (1,100,6,False):
        score += 1

#def test4():
    total+=1
    if student.end(4,'correct') == "I knew I could beat you, and in 4 tries too!":
        score += 1

#def test5():
    total+=1
    if student.end(6,'correct') == "I knew I could beat you, and in 6 tries too!":
        score += 1

#def test6():
    total+=1
    if student.end(7, 'correct') == "I ran out of tries! You bested me!":
        score += 1

#def test7():
    total+=1
    if student.end(1,'high') == "I ran out of tries! You bested me!":
        score += 1

#hidden tests
    total+=1
    if student.high_low(1,2,14,'correct',1,False) == (1,2,1,False):
        score += 1

    total+=1
    if student.end(1,'low') == "I ran out of tries! You bested me!":
        score += 1

    total+=1
    if student.high_low(1,100,50,'high',2,True) == (1,49,3,True):
        score += 1

    print(f"{score}/{total}")

if __name__ == '__main__':
    main()
