def main():
    total = 0
    score = 0

#def test1():
    total+=1
    if student.reverse("This is my message") == 'egassem ym si sihT':
        score += 1

#def test2():
    total+=1
    if student.reverse("egassem ym si sihT") == "This is my message":
        score += 1

#def test3():
    total+=1
    if student.reverse("[O.o]") == "]o.O[":
        score += 1

#hidden tests
    total+=1
    if student.reverse(".ecneciS retupmoC sehcaet nesnomiS .rM") == "Mr. Simonsen teaches Computer Sicence.":
        score += 1

    print(f"{score}/{total}")

if __name__ == '__main__':
    main()
