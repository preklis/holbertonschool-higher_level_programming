#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    ans = 0
    for i in range(1, argc):
        ans += int(argv[i])
    print(ans)
