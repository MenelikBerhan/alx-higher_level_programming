#!/usr/bin/python3
"""Module containing a script that reads `stdin` line by line
and computes metrics"""
import sys


try:
    count = 0
    total_size = 0
    status_dict = {}
    for line in sys.stdin:
        if count == 10:
            print("File size: {}".format(total_size))
            for k in sorted(status_dict.keys()):
                print("{}: {}".format(k, status_dict[k]))
            count = 0
        row = line.split()
        total_size += int(row[8])
        status = row[7]
        status_dict[status] = status_dict.get(status, 0) + 1
        count += 1
except KeyboardInterrupt:
    out = "File size: {}\n".format(total_size)
    status = ""
    for k in sorted(status_dict.keys()):
        status = status + "{}: {}\n".format(k, status_dict[k])
    print(out + status, end="")
    raise
