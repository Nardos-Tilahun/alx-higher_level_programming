#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(len(my_list[0:x])):
            print("{}".format(my_list[i]), end="")
        print()
        return (my_list[x-1])
    except IndexError:
        return (my_list[4])
