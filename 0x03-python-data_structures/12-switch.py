#!/usr/bin/python3
a = 89
b = 10
a, b = (a + b) - (b := a), a
print("a={:d} - b={:d}".format(a, b))
