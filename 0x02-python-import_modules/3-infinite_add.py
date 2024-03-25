#!/usr/bin/python3
from sys import argv


def main():
    print(sum([int(_) for _ in argv[1:]]))


if __name__ == "__main__":
    main()
