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
            print("File size: {:d}".format(total_size))
            for k in sorted(status_dict.keys()):
                print("{}: {:d}".format(k, status_dict[k]))
            count = 0
        row = line.split()
        total_size += int(row[8])
        status = row[7]
        status_dict[status] = status_dict.get(status, 0) + 1
        count += 1
except KeyboardInterrupt:
    out = "File size: {:d}\n".format(total_size)
    status = ""
    for k in sorted(status_dict.keys()):
        status = status + "{}: {:d}\n".format(k, status_dict[k])
    print(out + status, end="", flush=True)
    raise
