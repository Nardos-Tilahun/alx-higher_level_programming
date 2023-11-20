#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        a = fct(*args)
    except Exception as zde:
        print("Exception: {}".format(zde), file=sys.stderr)
        a = None
    else:
        return a
