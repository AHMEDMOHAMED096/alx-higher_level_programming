#!/usr/bin/python3
for char in range(122, 96, -1):
    if char % 2 == 0:
        print(chr(char), end="")
    elif char % 2 == 1:
        print(chr(char - 32), end="")
