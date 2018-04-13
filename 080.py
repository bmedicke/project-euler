#!/usr/bin/env python3

import decimal

"""
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""

decimal.getcontext().prec = 102 # enough precision to avoid rounding errors.
supersum = 0

for i in range(2, 100): # 0,1 and 100 have an int square root.
    sum = 0
    imaginary = decimal.Decimal(i).sqrt()

    try:
        imaginary.as_tuple()[1][1] # tuple out of range for rational numbers.
    except IndexError:
        continue

    digits = str(imaginary).replace('.', '')[:100]
    for digit in digits:
        sum += int(digit)
    print(i, digits, sum, sep='\t')
    supersum += sum
print(supersum)
