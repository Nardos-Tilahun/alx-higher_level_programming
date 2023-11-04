#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if my_string[i] == 'c':
            my_string[i] = 'C'
    return my_string
