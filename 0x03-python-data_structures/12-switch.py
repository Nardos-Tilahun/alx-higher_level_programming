#!/usr/bin/python3
a = 89
b = 10
a, b = int(b), int(a) if a is not None and b is not None else (a, b)
print("a={:d} - b={:d}".format(a, b))
