#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while x:
        try:
            print(my_list[i], end="")
        except IndexError:
            print()
            return i
        i += 1
        x -= 1
    print()
    return i
