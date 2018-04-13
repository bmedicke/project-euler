#!/usr/bin/env python3

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""


def r_shift(s, i):
    r = s[i:]+s[:i]
    return r

primes = []

for i in range(2, 1_000_000):
    prime = True

    for n in range(2, int(i**0.5+1)):
        if i % n == 0:
            prime = False
            break

    if prime:
        primes.append(i)

c_primes = 0

for prime in primes:
    length = len(str(prime))
    circular = True

    for i in range(1, length):
        p = r_shift(str(prime), i)

        if int(p) not in primes:
            circular = False
            break

    if circular:
        c_primes += 1

print(c_primes)
