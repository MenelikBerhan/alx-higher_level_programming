#!/usr/bin/python3
"""Module for solving the `The N queens puzzle`"""
import sys


def queens(size, i, a, b, c):
    """Finds solution for n-queens puzzle using Niklaus Wirth's solution"""
    if i < size:
        for j in range(size):
            if j not in a and i+j not in b and i-j not in c:
                yield from queens(size, i+1, a+[j], b+[i+j], c+[i-j])
    else:
        yield a


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
size = int(sys.argv[1])
ans = queens(size, 0, [], [], [])
print(type(ans))
coord = []

for solution in ans:
    ans_row = []
    for x, y in enumerate(solution):
        ans_row.append([x, y])
    coord.append(ans_row)

for solution in coord:
    print(solution)
