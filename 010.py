#!/usr/bin/env python3

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

sum = 0

for i in range(2, 2_000_000):
    prime = True
    for div in range(2, int(i**0.5+1)):
        if i % div == 0:
            prime=False
            break
    if prime:
        print(i)
        sum += i

print('sum', sum)
