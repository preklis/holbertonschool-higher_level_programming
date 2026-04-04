#!/usr/bin/python3
from calculator_1 import add,sub,mul,div
import sys
if __name__ == "__main__":
    argv=sys.argv
    if len(argv) == 1:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a=int(argv[1])
    b=int(argv[3])
    op=(argv[2])

    if op not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    match op:
        case "+":
            print("{} + {} = {}".format(a,b,add(a,b)))
        case "-":
            print("{} - {} = {}".format(a,b,sub(a,b)))
        case "*":
            print("{} * {} = {}".format(a,b,mul(a,b)))
        case "/":
            print("{} / {} = {}".format(a,b,div(a,b)))
