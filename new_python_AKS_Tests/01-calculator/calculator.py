#Mr. Simonsen
#14

def math(a,b):
    a = int(a)
    b = int(b)
    add = a+b
    sub = a-b
    mul = a*b
    div = round(a/b,2)
    flr = a//b
    mod = a%b
    rep = f"addition is {add}\nsubtraction is {sub}\nmultiplication is {mul}\n"
    rep += f"division is {div}\nfloor division {flr}\nmodulus division is {mod}"
    return rep

def main():
    a = input("enter a number: ")
    b = input("enter a second number: ")
    print(math(a,b))
