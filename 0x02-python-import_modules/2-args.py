#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    args_num = len(args)

    if args_num == 0:
        print("Number of arguments: .")
    elif args_num == 1:
        print("Number of argument: {}:".format(args_num))
        print("1: {}".format(args[0]))
    else:
        print("Number of arguments: {}:".format(args_num))
        for i in range(args_num):
            print("{}: {}".format(i + 1, args[i]))

