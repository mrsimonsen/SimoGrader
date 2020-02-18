def main():
    total = 0
    score = 0

#def test1():
    total+=1
    if student.splitter("This is a message.") == (["This", 'is', 'a', 'message.'], 4):
        score += 1

#def test2():
    total+=1
    if student.splitter("This is a message. ") == (["This", 'is', 'a', 'message.', ''], 5):
        score += 1

#def test3():
    total+=1
    if student.splitter("1234") == (['1234'],1):
        score += 1

#def test4():
    total+=1
    random.seed(0)
    if student.scrambler(["This", 'is', 'a', 'message.']) == 'a This is message.':
        score += 1

#hidden tests
    total+=1
    random.seed(14)
    if student.scrambler(["This", 'is', 'a', 'message.']) == 'is message. a This':
        score += 1

    print(f"{score}/{total}")

if __name__ == '__main__':
    main()
