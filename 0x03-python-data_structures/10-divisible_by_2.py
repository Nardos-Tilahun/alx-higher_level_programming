#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return
    newli = []
    for i in my_list:
        if i % 2 == 0:
            newli.append(True)
        else:
            newli.append(False)
    return newli
