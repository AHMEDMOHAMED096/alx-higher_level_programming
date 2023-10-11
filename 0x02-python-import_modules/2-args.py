#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    args_num = len(args)

    if args_num == 1:
        print("Number of argument: {}".format(args_num))
    else:
        print("Number of arguments: {}".format(args_num))

    for i in range(args_num):
        print("{}: {}".format(i + 1, args[i]))
