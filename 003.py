#!/usr/bin/env python3

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

n = 600851475143
p = 2
o = n**(0.5) # last possible prime is sqrt of our number.

while p < o:
    if n%p == 0:
        n /= p
        print(p)
    else:
        p += 1
