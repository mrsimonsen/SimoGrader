import pytest
import TC2 as student
import hs_helper as hs

def main():
    a = ''
    while a not in ('run','test','reset','read'):
        print("Choose an option:\n\tRun\n\tTest")
        print("\tReset (highscores file)\n\tRead (highscores file)")
        a = input("Your choice: ")
        a = a.lower()
    if a=="run":
        print("\n--Running Program--\n")
        student.main()
    elif a=="test":
        print("\n--Testing Program--\n")
        pytest.main(['-v'])
    elif a=='read':
        print("\n--Reading highscores file--\n")
        hs.read()
    elif a=='reset':
        print("\n--Resetting highsocres file--\n")
        hs.reset()

if __name__ == '__main__':
    main()
    print("\n--Operation Complete--")
