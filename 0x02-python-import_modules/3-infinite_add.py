#!/usr/bin/python3
if __name__ == "__main__":
    import sys
sum = 0
arglen = len(sys.argv) - 1
if arglen == 0:
    print("0")
else:
    for i in range(arglen):
        sum += int(sys.argv[i + 1])
    print("{}".format(sum))
