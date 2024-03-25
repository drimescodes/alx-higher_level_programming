#!/usr/bin/python3
def max_integer(my_list=[]):
    max_l = -float("inf")
    for i in my_list:
        max_l = i if i > max_l else max_l
    return max_l if my_list else None
