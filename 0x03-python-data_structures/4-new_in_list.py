#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = [x for x in my_list]
    return (
        new_list[:idx] + [element] + new_list[idx + 1:]
        if idx > -1 and idx < len(my_list)
        else new_list
    )
