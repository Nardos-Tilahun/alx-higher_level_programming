#!/usr/bin/python3
def pow(a, b):
    pro = 1
    for i in range(abs(b)):
        pro *= a
    if b < 0:
        return 1/pro
    return pro

