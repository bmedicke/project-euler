#!/usr/bin/env python3

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math
import sys

a = b = c = 0

for a in range(1, 1001):
    for b in range(1, 1001):
        if (a < b < c):
            continue

        c = math.sqrt(a**2 + b**2)
        try:
            str(c).split('.')[1][1]
            continue
        except IndexError:
            pass

        if int(a+b+c) == 1000:
            print(a, b, c, a+b+c)
            solution = a * b * c
            print(int(solution))
            sys.exit(0)
