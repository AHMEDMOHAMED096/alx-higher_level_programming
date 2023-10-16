#!/usr/bin/python3
def remove_char_at(str, n):
    if str == "":
        return str
    elif n < 0 or n > len(str):
        return str
    else:
        return str.replace(str[n], "")
