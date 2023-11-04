#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is not {}:
        return len(sentence), sentence[0]
    else:
        return 0, None
