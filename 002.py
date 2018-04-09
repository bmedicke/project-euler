#!/usr/bin/env python3

(a, b) = (1, 2)
sum = 2

while True:
    a = a + b
    b = a + b

    if (b > 4_000_000):
        break

    print(a, b)

    if (a % 2 == 0):
        sum += a

    if (b % 2 == 0):
        sum += b

print(sum)
