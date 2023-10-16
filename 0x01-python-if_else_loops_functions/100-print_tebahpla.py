#!/usr/bin/python3
for i in range(ord('z'), ord('A') - 1, -1):
    print("{}{}".format(chr(i + 32), chr(i)), end='')
