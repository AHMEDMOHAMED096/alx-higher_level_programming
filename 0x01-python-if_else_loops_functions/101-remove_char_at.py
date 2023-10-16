#!/usr/bin/python3
def remove_char_at(str, n):
    if str == "":
        return
    elif n < 0:
        return
    else:
        return str.replace(str[n], "")
