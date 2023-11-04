#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return
    l = len(my_list) - 1
    if l >= 0:
        maxi = my_list[0]
        for i in range(l):
            if my_list[i] > maxi:
                maxi = my_list[i]
        return maxi
