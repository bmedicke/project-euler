#!/usr/bin/env python3

numbers = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand',
}

sum = 0

for n in range(1, 1000):
    if n <= 20:
        spoken = numbers[n]
        print(n, spoken)
        sum += len(spoken)

    elif n < 100:
        single = str(n)[1]
        ten = str(n)[0]+'0'
        spoken = numbers[int(ten)] + numbers[int(single)]
        print(n, spoken)
        sum += len(spoken)

    else:
        single = str(n)[2]
        ten = str(n)[1]
        hundred = str(n)[0]
        if (single == '0') and (ten == '0'):
            spoken = numbers[int(hundred)] + numbers[100]
        elif int(single) + int(ten+'0') < 20:
            spoken = numbers[int(hundred)] + numbers[100] + 'and' + numbers[int(ten+'0') + int(single)]
        else:
            spoken = numbers[int(hundred)] + numbers[100] + 'and' + numbers[int(ten+'0')] + numbers[int(single)]
        print(n, spoken)
        sum += len(spoken)

spoken = 'one' + numbers[1000]
sum += len(spoken)
print(1000, spoken)

print(sum)
