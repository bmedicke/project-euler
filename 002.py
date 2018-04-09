#!/usr/bin/env python3

(a, b) = (1, 2)
sum = 2

while b < 4_000_000:
    a = a + b
    b = a + b

    print(a, b)

    for n in (a, b):
        if n%2 == 0:
            sum+=n

print(sum)
