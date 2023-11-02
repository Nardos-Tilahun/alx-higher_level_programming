#!/usr/bin/python3
if __name__ = "__main__":
    import sys

argvec = sys.argv
arglen = len(sys.argv - 1)
if arglen == 0:
    print("{} arguments.".format(arglen))
else:
    if arglen == 1:
        print("{} argument:".format(arglen))
    else:
        print("{} arguments:".format(arglen))
    for i in range(arglen):
            print("{}: {}".format(i + 1 , argvec[i + 1]))
