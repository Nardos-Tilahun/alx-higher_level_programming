#!/usr/bin/python3
def uppercase(str):
    for j in str:
        i = ord(j)
        if (i >= 97 and i <= 122):
            i = ord(chr(i - 32))
        print("{}".format(chr(i)), end="")
    print()
