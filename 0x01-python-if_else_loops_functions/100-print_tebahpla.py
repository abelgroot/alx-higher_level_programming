#!/usr/bin/python3
def print_tebahpla():
    for i in range(25, -1, -1):
        if i % 2 == 0:
            print(chr(ord('a') + i), end="")
        else:
            print(chr(ord('A') + i), end="")
