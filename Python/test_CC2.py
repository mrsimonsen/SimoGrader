import random

def main():
    total = 0
    score = 0

    #def test_talk1():
    total+=1;
    random.seed(14)
    a = student.Critter('bob')
    if a.talk() == "I'm bob and I feel okay now.\n":
        score +=1

    #def test_talk2():
    total+=1;
    random.seed(0)
    a = student.Critter('bob')
    if a.talk() == "I'm bob and I feel frustrated now.\n":
        score +=1

    #def test_eat1():
    total+=1;
    random.seed(14)
    a = student.Critter('bob')
    if a.eat(10) == "Brruppp.  Thank you." and a.hunger == 1:
        score +=1

    #def test_eat2():
    total+=1;
    random.seed(0)
    a = student.Critter('bob')
    a.eat(5)
    if a.hunger == 2:
        score +=1

    #def test_play1():
    total+=1;
    random.seed(14)
    a = student.Critter('bob')
    if a.play(10) == "Wheee!" and a.boredom == 1:
        score +=1

    #def test_play2():
    total+=1;
    random.seed(0)
    a = student.Critter('bob')
    a.play(5)
    if a.boredom == 2:
        score +=1

    #def test_str1():
    total+=1;
    random.seed(14)
    a = student.Critter('bob')
    if a.__str__() == 'Critter Object\nName: bob\nHunger: 1\nBoredom: 9\nMood: okay\n' or a.__str__() == 'Critter Object\nName: bob\nHunger: 9\nBoredom: 1\nMood: okay\n':
        score +=1

    #def test_str2():
    total+=1;
    random.seed(0)
    a = student.Critter('sue')
    if a.__str__() == 'Critter Object\nName: sue\nHunger: 6\nBoredom: 6\nMood: frustrated\n':
        score +=1


    #hidden tests
    total+=1;
    random.seed(0)
    a = student.Critter('john')
    a.play(10)
    a.eat(10)
    if a.__str__() == "Critter Object\nName: john\nHunger: 1\nBoredom: 2\nMood: happy":
        score += 1

    total+=1;
    random.seed(14)
    a = student.Critter('john')
    a.eat(10)
    a.play(10)
    if a.__str__() == "student.Critterritter Object\nName: john\nHunger: 2\nBoredom: 1\nMood: happy":
        score += 1


    print(f"{score}/{total}")

if __name__ == '__main__':
    main()
