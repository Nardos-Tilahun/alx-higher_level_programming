#!/usr/bin/python3
a = 89
b = 10
if a is not None and b is not None:
    a, b = int(b), int(a)
    print("a={:d} - b={:d}".format(a, b))
