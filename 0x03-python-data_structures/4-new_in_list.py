#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp_list = my_list.copy()
    if 0 <= idx < len(my_list):
        cp_list[idx] = element
    return cp_list
