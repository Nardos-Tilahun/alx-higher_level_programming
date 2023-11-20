#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    b = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            b += 1
            pass
    print()
    return x - b
