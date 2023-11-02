#!/usr/bin/python3
if __name__ = "__main__":
    import sys

argvec = sys.argv
arglen = len(sys.argv)
if arglen == 1:
    print("{} arguments.".format(arglen - 1))
else:
    if arglen == 2:
        print("{} argument:".format(arglen - 1))
    else:
        print("{} arguments:".format(arglen - 1))
    for i in range(len(argvec)):
        if i > 0:
            print("{}: {}".format(i , argvec[i]))
