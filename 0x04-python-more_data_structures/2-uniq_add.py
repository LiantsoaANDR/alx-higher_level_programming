#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    sumuq = 0
    for i in uniq:
        sumuq += i
    return sumuq
