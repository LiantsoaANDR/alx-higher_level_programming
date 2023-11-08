#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    best = 0
    for key in a_dictionary:
        if best < a_dictionary.get(key):
            best = a_dictionary.get(key)
    return best
