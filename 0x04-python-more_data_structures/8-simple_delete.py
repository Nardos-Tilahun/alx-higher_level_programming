#!/usr/bin/python3
def simple_delete(abc, key=""):
    if key in abc:
        del abc[key]
    return abc
