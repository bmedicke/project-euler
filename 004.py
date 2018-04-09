#!/usr/bin/env python3

palindromes = ([])

for x in range(100, 1000):
    for y in range(100, 1000):
        r = str(x*y)
        if r == r[::-1]:
            palindromes.append(int(r))

print(sorted(palindromes)[-1])
