#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return
    le = len(my_list) - 1
    if le >= 0:
        maxi = my_list[0]
        for i in range(le):
            if my_list[i + 1] > maxi:
                maxi = my_list[i + 1]
        return maxi
