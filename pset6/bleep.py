from cs50 import get_string
import sys

words = set()

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python bleep.py bannedwords.txt")

    file = open(sys.argv[1], "r") # load in set of banned words
    for line in file:
        words.add(line.rstrip("\n"))
    file.close()

    uncensored = get_string("What message would you like to censor? \n")

    censored = uncensored.split()

    for c in censored:
        if c.lower() in words:
            for i in range(len(c)):
                print("*", end="")
        else:
            print(c, end="")
        print(" ", end="")


if __name__ == "__main__":
    main()
    print()
