#!/usr/bin/python3

for c in range(97, 123):
    if c == 122:
        end = '\n'
    else:
        end = ''
    print(f"{c:c}", end=end)
    c += 1
