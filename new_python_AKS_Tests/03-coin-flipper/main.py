from subprocess import run
file = "coin_flipper"
test = "03"

def main():
    a = ''
    while a not in ('run','test'):
        print("Choose an option:\n\tRun\n\tTest")
        a = input("Your choice: ")
        a = a.lower()
    if a=="run":
        print("\n--Running Program--\n")
        run(["python3", f"{file}.py"])
    elif a=="test":
        print("\n--Testing Program--\n")
        run(["python3", f"test_{test}.py"])

if __name__ == '__main__':
    main()
    print("\n--Operation Complete--")
