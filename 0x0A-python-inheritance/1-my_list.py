#!/usr/bin/python3
''' this is  1-my_list'''


class MyList(list):
    '''  MyList class to print the sorted list '''

    def print_sorted(self):
        ''' Prints the sorted list'''
        print(sorted(self))
