def main():
    total = 0
    score = 0

#def test_1():
    total+=1;
    add = 3
    sub = -1
    mul = 2
    div = 0.5
    flr = 0
    mod = 1
    rep = f"addition is {add}\nsubtraction is {sub}\nmultiplication is {mul}\n"
    rep += f"division is {div}\nfloor division {flr}\nmodulus division is {mod}"
    if student.math('1','2')==rep:
        score += 1

#def test_2():
    total+=1;
    add = 17
    sub = 11
    mul = 42
    div = 4.67
    flr = 4
    mod = 2
    rep = f"addition is {add}\nsubtraction is {sub}\nmultiplication is {mul}\n"
    rep += f"division is {div}\nfloor division {flr}\nmodulus division is {mod}"
    if student.math('14','3')==rep:
        score += 1

    #hidden tests
    total+=1;
    add = 30
    sub = 10
    mul = 200
    div = 2
    flr = 2
    mod = 0
    rep = f"addition is {add}\nsubtraction is {sub}\nmultiplication is {mul}\n"
    rep += f"division is {div}\nfloor division {flr}\nmodulus division is {mod}"
    if student.math('20','10')==rep:
        score += 1
    print(f"{score}/{total}")

if __name__ == '__main__':
    main()
