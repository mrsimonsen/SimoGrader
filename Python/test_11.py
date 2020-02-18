def main():
    total = 0
    score = 0
    dict = {'Strength':10,
        'Dexterity':10,
        'Constitution':10,
        'Wisdom':10,
        'Intelligence':10,
        'Charisma':10,
        'Pool':5}


    #def test_add1():
    total+=1;
    sm = student.add('Wisdom', 5, dict)
    sa = dict['Wisdom']
    sp = dict['Pool']
    if (sm,sa,sp) == ('5 added to Wisdom', 15, 0):
        score += 1

    #def test_add2():
    total+=1;
    sm = student.add('Strength', 6, dict)
    sa = dict['Strength']
    sp = dict['Pool']
    if (sm,sa,sp) == ('6 is more points than you have left in your pool', 10, 0):
        score += 1

    #def test_add3():
    total+=1;
    sp = dict['Pool']
    sm = student.add('Health', 2, dict)
    if (sm,sp) == ('Health is not a valid attribute',0):
        score += 1

    #def test_remove1():
    total+=1;
    sm = student.remove('Intelligence', 10, dict)
    sa = dict['Intelligence']
    sp = dict['Pool']
    if (sm,sa,sp) == ('10 removed from Intelligence', 0, 10):
        score += 1

    #def test_remove2():
    total+=1;
    sm = student.remove('Constitution', 11, dict)
    sa = dict['Constitution']
    sp = dict['Pool']
    if (sm,sa,sp) == ('11 is more points than you have left in Constitution', 10, 10):
        score += 1

    #def test_remove3():
    total+=1;
    sm = student.remove('Bob', 2, dict)
    sp = dict['Pool']
    if (sm,sp) == ('Bob is not a valid attribute',10):
        score += 1

    #hidden tests
    total+=1;
    sm = student.remove('Dexterity', 5, dict)
    sa = dict['Dexterity']
    sp = dict['Pool']
    if (sm,sa,sp) == ('5 removed from Dexterity',5,15):
        score += 1

    total+=1;
    sm = student.add('Charisma', 2, dict)
    sa = dict['Charisma']
    sp = dict['Pool']
    if (sm,sa,sp) == ('2 added to Charisma',12,13):
        score += 1

    print(f"{score}/{total}")

if __name__ == '__main__':
    main()
