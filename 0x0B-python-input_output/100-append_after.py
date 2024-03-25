#!/usr/bin/python3
"""
A function that inserts a line of text to a file, after each line containing a
specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific
    string
    """
    with open(filename, "r+") as f:
        text = f.readlines()
        for i, line in enumerate(text):
            if search_string in line:
                text.insert(i + 1, new_string)
        f.seek(0)
        f.writelines(text)
