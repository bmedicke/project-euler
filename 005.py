#!/usr/bin/env python3

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

n = 1
while True:
    found = True
    for i in range(1, 21):
        if not n % i == 0:
            found = False
            # print(n, 'not divisible by', i)
            break
    if found:
        print(n)
        break
    n += 1
