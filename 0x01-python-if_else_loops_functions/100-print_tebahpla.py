#!/usr/bin/python3
print(
    "".join(
        [chr(c) if not c % 2 else chr(c - 32) for c in range(122, 96, -1)]
    ).format(""),
    end="",
)
