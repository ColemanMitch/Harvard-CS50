from cs50 import get_int

h = 0

while(True):
    h = get_int("Height: ")
    if(h >= 1 and h <=8):
        break;

for i in range(1, h+1):

    for k in range(h-i): # prints the spaces in front of left side
        print(" ", end="")

    for k in range(i): # prints left side hashes
        print("#", end="")

    print("  ", end=""); # two spaces in between the pyramids

    for j in range(i): # prints the right side of pyramid
        print("#", end="")

    print("")

        #print("\n", end="")




