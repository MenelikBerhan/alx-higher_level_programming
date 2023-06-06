#!/usr/bin/python3
for c in range(97, 123):
    print("{0:c}".format(0 if c == 113 or c == 101 else c), end='')
    c += 1
