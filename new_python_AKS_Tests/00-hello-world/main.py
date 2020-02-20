from subprocess import run
file = "hello_world.py"

def main():
    a = ''
    while a not in ('run','test'):
        print("Choose an option:\n\tRun\n\tTest")
        a = input("Your choice: ")
        a = a.lower()
    if a=="run":
        print("\n--Running Program--\n")
        run(["python3", "hello_world.py"])
    elif a=="test":
        print("\n--Testing Program--\n")
        run(["python3", "test_00.py"])

if __name__ == '__main__':
    main()
    print("\n--Operation Complete--")
