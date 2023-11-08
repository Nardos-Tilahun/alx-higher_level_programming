#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    arr = []
    for i in set_1:
        if i not in set_2:
            if i not in arr:
                arr.append(i)
    for j in set_2:
        if j not in arr:
            if j not in set_1:
                arr.append(j)

    return arr
