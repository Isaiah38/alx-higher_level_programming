#!/usr/bin/python3
for num in range(0, 99+1):
    if num == 99:
        print(f"{num}")
    else:
        print(f"{num:0>2d}", end = ", ")
