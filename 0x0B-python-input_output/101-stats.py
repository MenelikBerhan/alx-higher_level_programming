#!/usr/bin/python3
"""Module containing a script that reads `stdin` line by line
and computes metrics"""
import sys


count = 0
total_size = 0
status_dict = {}
stat_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
try:

    for line in sys.stdin:
        if count == 10:
            print("File size: {}".format(total_size))
            for k in sorted(status_dict):
                print("{}: {}".format(k, status_dict[k]))
            count = 1
        else:
            count += 1
        row = line.split()
        try:
            total_size += int(row[-1])
        except (IndexError, ValueError):
            pass
        # total_size += int(row[8])
        # status = row[7]
        # status_dict[status] = status_dict.get(status, 0) + 1
        try:
            if row[-2] in stat_codes:
                if status_dict.get(row[-2], -1) == -1:
                    status_dict[row[-2]] = 1
                else:
                    status_dict[row[-2]] += 1
        except IndexError:
            pass

    print("File size: {}".format(total_size))
    for k in sorted(status_dict):
        print("{}: {}".format(k, status_dict[k]))
except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for k in sorted(status_dict):
        print("{}: {}".format(k, status_dict[k]))
    raise
