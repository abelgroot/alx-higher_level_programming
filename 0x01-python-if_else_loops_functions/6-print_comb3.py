#!/usr/bin/python3
first = True
for i in range(10):
    for j in range(i + 1, 10):
        if not first:
            print(", ", end="")
        print("{:02d}".format(i * 10 + j), end="")
        first = False
print()
