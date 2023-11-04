#!/usr/bin/python3
def no_c(my_string):
    my_copy = my_string.copy()
    for i in range(len(my_copy)):
        if my_copy[i] == 'c':
            my_copy[i] = 'C'
    return my_copy
