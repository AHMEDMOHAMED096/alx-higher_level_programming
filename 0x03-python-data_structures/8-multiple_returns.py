#!/usr/bin/python3
def multiple_returns(sentence):
    output = (len(sentence), sentence[0])
    if sentence == "":
        return (0, None)
    else:
        return output
