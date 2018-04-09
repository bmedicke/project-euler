#!/usr/bin/env python3

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

i = 2
prime_counter = 1

while prime_counter <= 10_001:
    prime = True
    for n in range(2, int(i**.5)+1):
        if i % n == 0:
            prime = False
            break
    if prime:
        print(prime_counter, ':', i)
        prime_counter += 1
    i += 1
