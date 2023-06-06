#!/usr/bin/python3
def uppercase(str):
    for c in str:
        n = ord(c)
        print("{:c}".format(n - 32 if n >= 97 and n <= 122 else n), end='')
    print()
