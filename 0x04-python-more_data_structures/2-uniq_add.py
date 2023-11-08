#!/usr/bin/python3
def uniq_add(my_list=[]):
    arr = []
    sum = 0
    for i in my_list:
        if i not in arr:
            arr.append(i)
            sum += i
    return sum
