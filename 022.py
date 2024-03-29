#!/usr/bin/env python3

"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

names = []
with open('p022_names.txt') as f:
    for name in f.read().split(','):
        name = name.split('"')[1]
        sum = 0
        for char in name:
            n = ord(char)-64
            sum += n
        names.append((name, sum))
        if name == 'COLIN':
            print(name, sum)

names = sorted(names)

i = 0
points = 0
for name in names:
    i+=1
    points += name[1] * i

print(points)
