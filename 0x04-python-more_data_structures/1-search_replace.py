#!/usr/bin/python3
def search_replace(my_list, search, replace):
    arr = []
    for i in my_list:
        if (search == i):
            i = replace
        arr.append(i)
    return arr
