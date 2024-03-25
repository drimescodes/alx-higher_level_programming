#!/usr/bin/python3
"""
A module that defines a function that prints a text with 2 new lines after each
of these characters: '.', '?' and ':'
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?' and
    ':'
    Args:
        text (str): The text to print
    Raises:
        ypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    for c in ".?:":
        text = (c + "\n\n").join(
            [line.strip(" ") for line in text.split(c)]
        )
    print(text, end="")
