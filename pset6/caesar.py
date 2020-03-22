from cs50 import get_int, get_string
import sys


if len(sys.argv)!= 2:
    sys.exit("Usage: python caesar.py n")

n = int(sys.argv[1])
n%=26

pt = get_string("plaintext: ")

print("ciphertext: ", end="")
for c in pt:
    if ord(c) >= 65 and ord(c) <= 90:
        if ord(c) + n > 90: # for overlap
            print(chr(ord(c) + n - 26), end="")
        else:
            print(chr(ord(c) + n), end="")
    elif ord(c) >= 97 and ord(c) <= 122:
        if ord(c) + n > 122: # for overlap
            print(chr(ord(c) + n - 26), end="")
        else:
            print(chr(ord(c) + n), end="")
    else:
         print(c, end="")


print()
