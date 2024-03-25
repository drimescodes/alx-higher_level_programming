#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""
import sys
import signal
import re


def print_stats():
    """Prints the statistics"""
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))


file_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
try:
    for i, line in enumerate(sys.stdin, 1):
        try:
            words = line.split()
            file_size += int(words[-1])
            status_codes[words[-2]] += 1
            if i % 10 == 0:
                print_stats()
        except Exception:
            pass
    print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
