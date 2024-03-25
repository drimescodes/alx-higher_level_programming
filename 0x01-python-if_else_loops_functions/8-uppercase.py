#!/usr/bin/python3
def uppercase(str):
    print(
        "".join(
            [
                chr(ord(s) - 32) if ord(s) > 96 and ord(s) < 123 else s
                for s in str
            ]
        ).format("")
    )
