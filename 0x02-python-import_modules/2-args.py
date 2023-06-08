#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    n = len(sys.argv) - 1
    print("{:d} {}{}".format(n, "argument" if n == 1 else "arguments",
                             "." if n == 0 else ":"))
    i = 1
    for arg in sys.argv[1:]:
        print("{:d}: {}".format(i, arg))
        i += 1
