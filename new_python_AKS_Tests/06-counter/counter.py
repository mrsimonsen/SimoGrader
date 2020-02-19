#Mr. Simonsen
#14

def count(start, end, step):
    rep = ''
    if step > 0:
        end += 1
    else:
        end -= 1
    for i in range(start, end, step):
        rep += f"{i} "
    return rep

def main():
    start = int(input("What is the starting number? "))
    end = int(input("What is the ending number? "))
    step = int(input("How much should I cound by? "))
    print(count(start,end,step))
