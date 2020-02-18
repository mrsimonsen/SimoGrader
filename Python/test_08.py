def main():
    total = 0
    score = 0

#def test1():
    total+=1
    if student.make_tri("@",3) == "\n@ \n@ @ \n@ @ @ \n":
        score += 1

#def test2():
    total+=1
    if student.make_tri("%", 5) == "\n% \n% % \n% % % \n% % % % \n% % % % % \n":
        score += 1

#def test3():
    total+=1
    if student.make_tri("m", 4) == "\nm \nm m \nm m m \nm m m m \n":
        score += 1

#def test4():
    total+=1
    if student.make_tri("*", 3) == "\n* \n* * \n* * * \n":
        score += 1

#hidden test
    total+=1
    if student.make_tri('-',7) == "\n- \n- - \n- - - \n- - - -\n- - - - -\n- - - - - -\n- - - - - - -\n":
        score+=1
    print(f"{score}/{total}")

if __name__ == '__main__':
    main()
