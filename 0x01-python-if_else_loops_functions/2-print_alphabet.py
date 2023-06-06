#!/usr/bin/python3
for c in range(97, 123):
    print("{0:c}".format(c), end='' if c < 122 else '\n')
    c += 1
