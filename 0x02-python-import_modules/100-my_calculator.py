#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    import calculator_1 as calc
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    ops = {'+': calc.add, '-': calc.sub, '*': calc.mul, '/': calc.div}
    args = sys.argv
    print("{} {} {} = {}".format(args[1], args[2], args[3],
                                 ops[args[2]](int(args[1]), int(args[3]))))
