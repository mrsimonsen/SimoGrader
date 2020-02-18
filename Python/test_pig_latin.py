def main():
    total = 0
    score = 0

#def test1():
    total+=1
    if student.ay_end("speaker",2)=="eakerspay ":
        score += 1
#def test2():
    total+=1
    if student.ay_end("HAPPY!",1)=="APPYHay! ":
        score += 1
#def test3():
    total+=1
    if student.way_end("eggs")=="eggsway ":
        score += 1
#def test4():
    total+=1
    if student.way_end("Apple!")=="Appleway! ":
        score += 1
#def test5():
    total+=1
    if student.translator("This, a Platypus, is.")=="Isthay, away atypusplay, isway. ":
        score += 1

#hidden tests
    total+=1
    if student.translator("Some message this is!")=="Omesay essagemay isthay isway!":
        score += 1
    total += 1
    if student.translator("May the Force be with you!")=="Aymay ethay orcefay ebay ithway ouyay!":
        score += 1

    print(f"{score}/{total}")

if __name__ == '__main__':
    main()
