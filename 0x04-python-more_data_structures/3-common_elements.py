#!/usr/bin/python3
def common_elements(set_1, set_2):
    arr = []
    for i in set_1:
        if i in set_2:
            if i not in arr:
                arr.append(i)
    return arr
