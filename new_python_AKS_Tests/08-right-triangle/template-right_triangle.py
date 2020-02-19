#Name
#Period

def make_tri(tri_char, tri_height):
    tri = "\n"
    tri += "* \n"
    tri += "* * \n"
    tri += "* * * \n"
    return tri

def main():
      tri_char = input("Enter a character: ")
      tri_height = int(input("Enter triangle height: "))
      # Draw right triangle
      print(make_tri(tri_char, tri_height))

if __name__ == '__main__':
    main()
