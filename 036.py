#!/usr/bin/env python3

sum = 0
for i in range(1, 1_000_000):
    s = str(i)
    if s == s[::-1]:
        b = str(bin(i))[2:]
        if b == b[::-1]:
            print(s, b)
            sum += i
print(sum)
