#!/usr/bin/python3
print(
    "".join([chr(_) for _ in range(97, 123) if _ != 101 and _ != 113]).format(
        ""
    ),
    end="",
)
