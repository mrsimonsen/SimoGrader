#Mr. Simonsen
#14

def make_tri(tri_char, tri_height):
    tri = ""
    for i in range(tri_height+1):
        tri += f"{tri_char} "*i +"/n"
    return tri


def main():
      tri_char = input("Enter a character: ")
      tri_height = int(input("Enter triangle height: "))
      # Draw right triangle
      print(make_tri(tri_char, tri_height))

if __name__ == '__main__':
    main()
