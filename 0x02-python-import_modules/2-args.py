#!/usr/bin/python3
from sys import argv


def main():
    print(
        "{} argument{}{}".format(
            len(argv) - 1,
            "s" if len(argv) != 2 else "",
            ":" if len(argv) - 1 else ".",
        )
    )
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
