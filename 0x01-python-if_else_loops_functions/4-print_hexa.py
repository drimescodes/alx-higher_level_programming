#!/usr/bin/python3
print(
    "\n".join([f"{i} = {hex(i)}" for i in range(0, 99)]).format("")
)  # NOTE: Had to use '.format("")', project requirement :)
