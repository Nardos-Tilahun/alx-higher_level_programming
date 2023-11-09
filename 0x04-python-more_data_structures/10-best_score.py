#!/usr/bin/python3
def best_score(new):
    if not new:
        return (None)

    return (max(new, key=new.get))
