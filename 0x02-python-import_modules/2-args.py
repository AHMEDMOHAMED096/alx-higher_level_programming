#!/usr/bin/python3

import sys


def print_arguments(argv):
    num_args = len(argv)

    if num_args == 0:
        print(f"{num_args} arguments.")
    elif num_args == 1:
        print(f"{num_args} argument:")
        print("1:", argv[0])
    else:
        print(f"{num_args} arguments:")
        for i, arg in enumerate(argv):
            print(i+1, ":", arg)


if __name__ == "__main__":
    print_arguments(sys.argv[1:])
