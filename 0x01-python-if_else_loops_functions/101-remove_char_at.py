#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    for i in str:
        if (n < len(str) and str[n] == i):
            if (n < 0):
                str2 += i
            continue
        str2 += i
    return str2
