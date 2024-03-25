#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div


def main():
    if len(argv) != 4:
        err("Usage: ./100-my_calculator.py <a> <operator> <b>", 1)
    op_dict = {"+": add, "-": sub, "*": mul, "/": div}
    if argv[2] not in op_dict.keys():
        err("Unknown operator. Available operators: +, -, * and /", 1)
    print(
        "{} {} {} = {}".format(
            argv[1],
            argv[2],
            argv[3],
            op_dict[argv[2]](int(argv[1]), int(argv[3])),
        )
    )


def err(msg, code):
    print(msg)
    exit(code)


if __name__ == "__main__":
    main()
