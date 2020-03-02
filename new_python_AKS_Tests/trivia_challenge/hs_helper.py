import pickle

def reset():
    hs = [(3,'ABC'),(2,'DEF'),(1,'GHI')]
    f = open('highscores.dat','wb')
    pickle.dump(hs, f)
    f.close()
    print('--reset complete--')

def read():
    f = open('highscores.dat','rb')
    hs = pickle.load(f)
    print(hs)
