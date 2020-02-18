def main():
    total = 0
    score = 0

#def test_1():
    total+=1
    if student.hello('Mr. Simonsen', 1) == 'Hello World!\nMr. Simonsen\nPeriod 1':
        score += 1

#def test_2():
    total+=1
    if student.hello('NUAMES', 14) == 'Hello World!\nNUAMES\nPeriod 14':
        score += 1
#hidden test
    total+=1
    if student.hello('D13',213) == 'Hello World!\nD13\nPeriod 213':
        score+=1
    print(f"{score}/{total}")

if __name__ == '__main__':
    main()
